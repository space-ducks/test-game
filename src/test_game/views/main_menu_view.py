import arcade
from arcade.gui import (
    UIAnchorLayout,
    UIGridLayout,
    UIManager,
    UITextureButton,
)
from pyglet.graphics import Batch
from pathlib import Path

import test_game
import test_game.load_svg as svg

# TEXTURES = test_game.load_textures()
# TEX_BANNER = test_game.lookup_texture(TEXTURES, "ui_double", "banner_classic_curtainimg.png")
# TEX_BUTTON = test_game.lookup_texture(TEXTURES, "rpg_ui", "buttonLong_brown.png")
# TEX_BUTTON_PRESS = test_game.lookup_texture(TEXTURES, "rpg_ui", "buttonLong_brown_pressed.png")
arcade.load_font(Path(__file__).parent.parent / "assets/fonts/RubikSprayPaint-Regular.ttf")
FONT_TITLE = "Rubik Spray Paint"
arcade.load_font(Path(__file__).parent.parent / "assets/fonts/MouseMemoirs-Regular.ttf")
FONT_TEXT = "Mouse Memoirs"

TESTURES = svg.load_textures()
TEST_TEX = svg.lookup_texture(TESTURES, "hex_tiles", 0, 3)


class MainMenuView(arcade.View):
    """
    Main Menu View for `test_game`.

    Inherits from `arcade.View`.
    """

    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.ALICE_BLUE

        self.scene = arcade.Scene()
        self.text_batch = Batch()
        self.ui = UIManager()

    def setup(self):
        # background sprite loading
        self.scene.add_sprite_list("background")

        banner = arcade.Sprite()
        banner.texture = TEST_TEX
        banner.center_x = test_game.WINDOW_WIDTH / 2
        banner.center_y = test_game.WINDOW_HEIGHT / 2

        # self.title = arcade.Text(
        #     "Test Game",
        #     banner.center_x,
        #     banner.center_y + 3,
        #     font_name="FONT_TITLE",
        #     font_size=20,
        #     bold=True,
        #     anchor_x="center",
        #     anchor_y="center",
        #     batch=self.text_batch,
        # )

        self.scene.add_sprite("background", banner)

        # # menu sprite loading
        # self.scene.add_sprite_list("menu")

        # menu_grid = UIGridLayout(
        #     x=test_game.WINDOW_WIDTH // 2,
        #     y=test_game.WINDOW_HEIGHT // 2,
        #     align_vertical="top",
        #     column_count=1,
        #     row_count=4,
        #     vertical_spacing=TEX_BUTTON.height // 2,
        #     horizontal_spacing=10,
        # )

        # self.ui.add(UIAnchorLayout(children=[menu_grid]))

        # menu_grid.add(
        #     UITextureButton(texture=TEX_BUTTON, texture_hovered=TEX_BUTTON_PRESS, text="Start Game"), row=0, column=0
        # )
        # menu_grid.add(
        #     UITextureButton(texture=TEX_BUTTON, texture_pressed=TEX_BUTTON_PRESS, text="Continue Game"), row=1, column=0
        # )
        # menu_grid.add(
        #     UITextureButton(texture=TEX_BUTTON, texture_pressed=TEX_BUTTON_PRESS, text="Load Save"), row=2, column=0
        # )
        # menu_grid.add(
        #     UITextureButton(texture=TEX_BUTTON, texture_pressed=TEX_BUTTON_PRESS, text="Exit"), row=3, column=0
        # )

    def on_draw(self) -> bool | None:
        self.clear()

        self.scene.draw()
        self.text_batch.draw()
        self.ui.draw()

    def on_update(self, delta_time: float) -> bool | None:
        pass

    def on_key_press(self, symbol: int, modifiers: int) -> bool | None:
        pass

    def on_key_release(self, symbol: int, modifiers: int) -> bool | None:
        pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> bool | None:
        pass


if __name__ == "__main__":
    from test_game.main import main

    main()
