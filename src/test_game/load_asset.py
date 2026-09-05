"""
This module loads assets from a set of spritesheets.
"""

import xml.etree.ElementTree as ET
from pathlib import Path

import arcade

spritesheet_list: dict[str, list[Path]] = {
    "bg_elements": [
        Path(__file__).parent / "assets/kenney_background-elements/Spritesheet/bgElements_spritesheet.png",
        Path(__file__).parent / "assets/kenney_background-elements/Spritesheet/bgElements_spritesheet.xml",
    ],
    "hex-buildings": [
        Path(__file__).parent / "assets/kenney_hexagon-buildings/Spritesheet/sheet.png",
        Path(__file__).parent / "assets/kenney_hexagon-buildings/Spritesheet/sheet.xml",
    ],
    "hex-tiles": [
        Path(__file__).parent / "assets/kenney_hexagon-pack/Spritesheets/hexagonAll_sheet.png",
        Path(__file__).parent / "assets/kenney_hexagon-pack/Spritesheets/hexagonAll_sheet.xml",
    ],
    "rpg-ui": [
        Path(__file__).parent / "assets/kenney_ui-pack-rpg-expansion/Spritesheet/uipack_rpg_sheet.png",
        Path(__file__).parent / "assets/kenney_ui-pack-rpg-expansion/Spritesheet/uipack_rpg_sheet.xml",
    ],
}


def conv_int(val) -> int:
    """
    Converts an arbitrary value to type: int
    if it can be converted to one.

    Parameters
    ----------
    val : Any
        Value to be converted

    Returns
    -------
    int
        Converted integer value.

    Raises
    ------
    ValueError
        Raises if value cannot be converted to type: int.
    """
    try:
        return int(val)
    except (TypeError, ValueError):
        raise ValueError(f"{val} could not be converted to type: int.") from None


def load_textures(sheet_files: dict[str, list[Path]] = spritesheet_list) -> dict:
    """
    Loads textures from spritesheet files, returning them
    as a dictionary organized by spritesheet name and
    texture name.

    Parameters
    ----------
    sheet_files : dict[str, list[Path]], optional
        dictionary of , by default spritesheet_list

    Returns
    -------
    dict
        Organized textures
    """

    texture_dict = {}

    for key, entry in sheet_files.items():
        texture_dict[key] = {}
        png_file = entry[0]
        xml_file = entry[1]

        spritesheet = arcade.load_texture(png_file)
        textures = ET.parse(str(xml_file)).findall("SubTexture")

        for texture in textures:
            name = str(texture.get("name"))
            x = conv_int(texture.get("x"))
            y = conv_int(texture.get("y"))
            w = conv_int(texture.get("width"))
            h = conv_int(texture.get("height"))

            texture_dict[key][name] = spritesheet.crop(x, y, w, h)

    return texture_dict


def lookup_texture(
    textures: dict, pack: str, name: str, sheet_files: dict[str, list[Path]] = spritesheet_list
) -> arcade.Texture:
    """_summary_

    Parameters
    ----------
    textures : dict
        _description_
    pack : str
        _description_
    name : str
        _description_
    sheet_files : dict[str, list[Path]], optional
        _description_, by default spritesheet_list

    Returns
    -------
    arcade.Texture
        _description_

    Raises
    ------
    LookupError
        _description_
    """
    try:
        return textures[pack][name]
    except Exception:
        raise LookupError(f"Texture {name} in {pack} pack could not be found.") from None


if __name__ == "__main__":
    textures = load_textures()
    print(lookup_texture(textures, "bg_elements", "tree280.png"))
