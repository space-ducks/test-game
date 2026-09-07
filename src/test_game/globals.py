"""Global variables and parameters."""

from pathlib import Path

# Spritesheet globals
spritesheets: dict[str, Path] = {
    "bg_elements" : Path(__file__).parent / "assets/kenney_background-elements/sheet.svg",
    "hex_buildings" : Path(__file__).parent / "assets/kenney_hexagon-buildings/sheet.svg",
    "hex_pack" : Path(__file__).parent / "assets/kenney_hexagon-pack/sheet.svg",
    "hex_tiles" : Path(__file__).parent / "assets/kenney_hexagon-tiles/sheet.svg",
    "enemies" : Path(__file__).parent / "assets/kenney_platformer-art-extended-enemies/sheet.svg",
    "character" : Path(__file__).parent / "assets/kenney_platformer-characters/sheet.svg",
    "ui" : Path(__file__).parent / "assets/kenney_ui-pack-adventure/sheet.svg",
    "ui_platformer" : Path(__file__).parent / "assets/kenney_platformer-pack-remastered/sheet.svg",
    "ui_rpg" : Path(__file__).parent / "assets/kenney_ui-pack-rpg-expansion/sheet.svg",
}
"""
Spritesheets that can be imported and used in this project.

|Key|Description|
|:---|:---|
|"bg_elements"|[Kenney Background Elements](https://kenney.nl/assets/background-elements)|
|"hex_buildings"|[Kenney Hexagon Buildings](https://kenney.nl/assets/hexagon-buildings)|
|"hex_pack"|[Kenney Hexagon Pack](https://kenney.nl/assets/hexagon-pack)|
|"hex_tiles"|[Kenney Hexagon Tiles](https://kenney.nl/assets/hexagon-tiles)|
|"enemies"|[Kenney Platformer Art Extended Enemies](https://kenney.nl/assets/platformer-art-extended-enemies)|
|"character"|[Kenney Platformer Characters](https://kenney.nl/assets/platformer-characters)|
|"ui"|[Kenney UI Pack - Adventure](https://kenney.nl/assets/ui-pack-adventure)|
|"ui_platformer"|[Kenney Platformer Pack Remastered](https://kenney.nl/assets/platformer-pack-remastered)|
|"ui_rpg"|[Kenney UI Pack (RPG Expansion)](https://kenney.nl/assets/ui-pack-rpg-expansion)|
"""

# Window globals
WINDOW_WIDTH = 1280
"""Default window width (pixels)."""

WINDOW_HEIGHT = 720
"""Default window height (pixels)."""

# Player globals
PLAYER_START_LEVEL = 1
"""Player starting level."""

PLAYER_START_EXP = 0
"""Player starting experience."""

PLAYER_START_HP = 10
"""Player starting health points."""

PLAYER_START_GOLD = 0
"""Player starting gold."""

PLAYER_START_CLS = None
"""Player starting class."""

# Enemy globals

# Level globals
