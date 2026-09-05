"""
Loads assets from a set of spritesheets.
"""

import xml.etree.ElementTree as ET

import arcade

import test_game as game


def _conv_int(val) -> int:
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
    except Exception:
        raise ValueError(f"{val} could not be converted to type: int.") from None


def load_textures() -> dict:
    """
    Loads textures from spritesheet files in `globals.py`,
    returning them as a dictionary organized by spritesheet
    name and texture name.

    Returns
    -------
    dict
        Organized textures
    """

    texture_dict = {}

    for key, entry in game.spritesheets.items():
        texture_dict[key] = {}
        png_file = entry[0]
        xml_file = entry[1]

        spritesheet = arcade.load_texture(png_file)
        textures = ET.parse(str(xml_file)).findall("SubTexture")

        for texture in textures:
            name = str(texture.get("name"))
            x = _conv_int(texture.get("x"))
            y = _conv_int(texture.get("y"))
            w = _conv_int(texture.get("width"))
            h = _conv_int(texture.get("height"))

            texture_dict[key][name] = spritesheet.crop(x, y, w, h)

    return texture_dict


def lookup_texture(textures: dict, pack: str, name: str) -> arcade.Texture:
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
    name : str
        Name of texture.

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
        return textures[pack][name]
    except Exception:
        raise LookupError(f"Texture {name} in {pack} pack could not be found.") from None


if __name__ == "__main__":
    textures = load_textures()
