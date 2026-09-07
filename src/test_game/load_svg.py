"""
Loads assets from a set of spritesheets.
"""

import io
import xml.etree.ElementTree as ET
import arcade
import resvg_py
import test_game
from PIL import Image
from svgpathtools import parse_path
from pathlib import Path

SVG_NS = "http://www.w3.org/2000/svg"

def _path_bounds(group) -> tuple | None:
    """
    Determines bounding box for an svg group
    of shapes.

    Parameters
    ----------
    group
        svg group.

    Returns
    -------
    tuple
        Bounding box coordinates, organized as
        (xmin, xmax, ymin, ymax).
        
    """
    bounds = []

    for path in group.findall(f"{{{SVG_NS}}}path"):
        d = path.get("d", "")
        if not d:
            continue

        parsed = parse_path(d)

        xmin, xmax, ymin, ymax = parsed.bbox()
        bounds.append((xmin, ymin, xmax, ymax))

    if not bounds:
        return None

    return (
        min(x[0] for x in bounds),
        min(x[1] for x in bounds),
        max(x[2] for x in bounds),
        max(x[3] for x in bounds),
    )

def load_textures() -> dict:
    """
    Loads textures from spritesheet files in `globals.py`,
    returning them as a dictionary organized by spritesheet
    name and texture name.

    Returns
    -------
    dict
        Organized textures.
    """
    texture_dict = {}

    for key, entry in test_game.spritesheets.items():
        texture_dict[key] = {}

        # Group svg by <g> group tag
        root = ET.parse(entry).getroot()
        groups = [element for element in root if element.tag == f"{{{SVG_NS}}}g"]

        for index, group in enumerate(groups):

            # Crop svg viewbox to just one sprite group
            bounds = _path_bounds(group)
            if bounds is None:
                continue
            min_x, min_y, max_x, max_y = bounds

            sprite_svg = ET.Element(
                root.tag,
                {
                    "xmlns": SVG_NS,
                    "viewBox": f"{min_x} {min_y} {max_x - min_x} {max_y - min_y}",
                    "width": str(max_x - min_x),
                    "height": str(max_y - min_y),
                },
            )

            # Keep any styles applied to svg
            for child in root:
                if child.tag in (
                        f"{{{SVG_NS}}}style",
                        f"{{{SVG_NS}}}defs"
                ):
                    sprite_svg.append(child)

            # Add svg to dictionary
            sprite_svg.append(group)

            texture_dict[key][index] = ET.tostring(sprite_svg, encoding="unicode")

    return texture_dict


def lookup_texture(textures: dict, pack: str, index: int, scale: float=1) -> arcade.Texture:
    """
    Looks up a specific texture.

    Parameters
    ----------
    textures : dict
        Textures
    pack : str
        Name of texture pack, see
        `test_game.globals.spritesheets.keys()`
        for available packs.
    name : int
        Index of texture.
    scale : float, optional
        Resolution scale, by default 1

    Returns
    -------
    arcade.Texture
        Texture.

    Raises
    ------
    LookupError
        Raises if texture cannot be found.
    """
    try:
        svg_data = textures[pack][index]
    except KeyError:
        raise LookupError(f"Texture {index} in {pack} pack could not be found.") from None

    # Convert svg to png to be used with arcade
    png_data = resvg_py.svg_to_bytes(svg_data, zoom=scale)
    image = Image.open(io.BytesIO(png_data))

    return arcade.Texture(image=image)


if __name__ == "__main__":
    textures = load_textures()
    # for img in textures["ui_platformer"]:
    #     out_path = Path(__file__).parent / f"assets/kenney_platformer-pack-remastered/PNGs/{img:03d}.png"
    #     png = lookup_texture(textures, "ui_platformer", img).image.save(out_path)
