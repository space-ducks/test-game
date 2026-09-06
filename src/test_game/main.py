import arcade

import test_game


def main():
    window = arcade.Window(test_game.WINDOW_WIDTH, test_game.WINDOW_HEIGHT)
    game = test_game.MainMenuView()

    window.show_view(game)


if __name__ == "__main__":
    main()
