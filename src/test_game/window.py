import arcade
import test_game

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Test Game"

class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()
        self.scene = arcade.Scene()
        self.textures = test_game.load_textures()

        self.background_color = arcade.color.ALICE_BLUE

    def setup(self):
        self.scene.add_sprite_list("background")
        self.scene.add_sprite_list("terrain")
        self.scene.add_sprite_list("enemies")
        self.scene.add_sprite_list("character")

        for col in range(13):
            for row in range(9):
                tile = arcade.Sprite()
                if row == 0:
                    tile.texture = test_game.lookup_texture(self.textures, "hex_pack", "dirt_01.png")
                else:
                    tile.texture = test_game.lookup_texture(self.textures, "hex_pack", "grass_01.png")
                
                if row % 2 == 0:
                    x_offset = tile.width / 2
                else:
                    x_offset = 0
                tile.center_x = col * tile.width + x_offset
                tile.center_y = row * (tile.height * 3 / 4)
                self.scene.add_sprite("terrain", tile)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Call draw() on all your sprite lists below
        self.scene.draw()

    def on_update(self, delta_time):
        pass

def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()
    game.setup()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()



if __name__ == "__main__":
    main()