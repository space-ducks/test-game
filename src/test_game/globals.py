"""Global variables and parameters."""

from pathlib import Path

spritesheets: dict[str, list[Path]] = {
    "bg_elements": [
        Path(__file__).parent / "assets/kenney_background-elements/Spritesheet/bgElements_spritesheet.png",
        Path(__file__).parent / "assets/kenney_background-elements/Spritesheet/bgElements_spritesheet.xml",
    ],
    "hex_buildings": [
        Path(__file__).parent / "assets/kenney_hexagon-buildings/Spritesheet/sheet.png",
        Path(__file__).parent / "assets/kenney_hexagon-buildings/Spritesheet/sheet.xml",
    ],
    "hex_pack": [
        Path(__file__).parent / "assets/kenney_hexagon-pack/Spritesheets/hexagonAll_sheet.png",
        Path(__file__).parent / "assets/kenney_hexagon-pack/Spritesheets/hexagonAll_sheet.xml",
    ],
    "hex_tiles": [
        Path(__file__).parent / "assets/kenney_hexagon-tiles/Spritesheet/complete.png",
        Path(__file__).parent / "assets/kenney_hexagon-tiles/Spritesheet/complete.xml",
    ],
    "ui": [
        Path(__file__).parent / "assets/kenney_ui-pack-adventure/Spritesheet/spritesheet-default.png",
        Path(__file__).parent / "assets/kenney_ui-pack-adventure/Spritesheet/spritesheet-default.xml",
    ],
    "rpg_ui": [
        Path(__file__).parent / "assets/kenney_ui-pack-rpg-expansion/Spritesheet/uipack_rpg_sheet.png",
        Path(__file__).parent / "assets/kenney_ui-pack-rpg-expansion/Spritesheet/uipack_rpg_sheet.xml",
    ],
}
"""
Spritesheets that can be imported and used in this project.

|Key|Description|
|:---|:---|
|"bg_elements"|[Kenney Background Elements](https://kenney.nl/assets/background-elements)|
|"hex_buildings"|[Kenney Hexagon Buildings](https://kenney.nl/assets/hexagon-buildings)|
|"hex_pack"|[Kenney Hexagon Pack](https://kenney.nl/assets/hexagon-pack)|
|"hex_tiles"|[Kenney Hexagon Tiles](https://kenney.nl/assets/hexagon-tiles)|
|"ui"|[Kenney UI Pack - Adventure](https://kenney.nl/assets/ui-pack-adventure)|
|"rpg_ui"|[Kenney UI Pack (RPG Expansion)](https://kenney.nl/assets/ui-pack-rpg-expansion)|
"""

WINDOW_WIDTH = 1280
"""Default window width (pixels)."""

WINDOW_HEIGHT = 720
"""Default window height (pixels)."""
