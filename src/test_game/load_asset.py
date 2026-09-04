"""
This module loads assets from a set of spritesheets.
"""

from pathlib import Path
from typing import Type
import xml.etree.ElementTree as ET
import arcade

spritesheet_list: dict[str, list[Path]] = {
    "bg_elements" : [
        Path(__file__).parent / "assets/kenney_background-elements/Spritesheet/bgElements_spritesheet.png",
        Path(__file__).parent / "assets/kenney_background-elements/Spritesheet/bgElements_spritesheet.xml"
    ],
    "hex-buildings" : [
        Path(__file__).parent / "assets/kenney_hexagon_buildings/Spritesheet/sheet.png",
        Path(__file__).parent / "assets/kenney_hexagon_buildings/Spritesheet/sheet.xml"
    ],
    "hex-tiles" : [
        Path(__file__).parent / "assets/kenney_hexagon-pack/Spritesheets/hexagonAll_sheet.png",
        Path(__file__).parent / "assets/kenney_hexagon-pack/Spritesheets/hexagonAll_sheet.xml"
        
    ],
    "rpg-ui" : [
        Path(__file__).parent / "assets/kenney_ui-pack-rpg-expansion/Spritesheet/uipack_rpg_sheet.png",
        Path(__file__).parent / "assets/kenney_ui-pack-rpg-expansion/Spritesheet/uipack_rpg_sheet.xml"
    ]
}

def conv_int(val, val_type:Type=str) -> int:
    r"""
    Converts an arbitrary value to type: int
    if it can be converted to one.

    $$a+b=c$$

    !!! warning
        uh oh

    Parameters
    ----------
    val : Any
        _description_
    val_type : Type, optional
        _description_, by default str

    Returns
    -------
    int
        _description_

    Raises
    ------
    ValueError
        _description_
    """
    if isinstance(val, val_type):
        return int(val)
    else: raise ValueError

def load_textures():
    pass

def lookup_texture(pack:str, name:str):
    pass

spritesheet = arcade.load_texture(spritesheet_list["bg_elements"][0])

xml_file = ET.parse(str(spritesheet_list["bg_elements"][1]))
textures = xml_file.findall("SubTexture")
texture_lookup: dict[str, arcade.Texture] = {}

for texture in textures:
    name = str(texture.get("name"))
    x = conv_int(texture.get("x"))
    y = conv_int(texture.get("y"))
    w = conv_int(texture.get("width"))
    h = conv_int(texture.get("height"))

    texture_lookup[name] = spritesheet.crop(x, y, w, h)

print(texture_lookup["tree28.png"])