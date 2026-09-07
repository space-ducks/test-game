import arcade
import pyglet
import test_game


def main():
    pyglet.options.dpi_scaling = "real"

    window = arcade.Window(test_game.WINDOW_WIDTH, test_game.WINDOW_HEIGHT)
    game = test_game.MainMenuView()
    game.setup()

    window.show_view(game)

    arcade.run()


if __name__ == "__main__":
    main()
