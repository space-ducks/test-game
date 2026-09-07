import arcade


class MainMenuView(arcade.View):
    """
    Main Menu View for `test_game`.

    Inherits from `arcade.View`.
    """

    def __init__(self):
        super().__init__()

    def on_draw(self) -> bool | None:
        self.clear()

    def on_update(self, delta_time: float) -> bool | None:
        pass

    def on_key_press(self, symbol: int, modifiers: int) -> bool | None:
        pass

    def on_key_release(self, symbol: int, modifiers: int) -> bool | None:
        pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> bool | None:
        pass
