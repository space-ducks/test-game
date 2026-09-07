import test_game


class Player:
    """
    Player class for `test_game`.

    Attributes
    ----------
    level : int
        Player level.
    exp : int
        Player experience towards next level.
    hp : int
        Player current health points.
    hp_max : int
        Player maximum health points.
    cls : _PlayerClass | None
        Player class.
    items : dict
        Player current items.
    """

    def __init__(self) -> None:
        self.level: int = test_game.PLAYER_START_LEVEL
        self.exp: int = test_game.PLAYER_START_EXP
        self.hp: int = test_game.PLAYER_START_HP
        self.hp_max = test_game.PLAYER_START_HP
        self.gold = test_game.PLAYER_START_GOLD
        self.cls: _PlayerClass | None = test_game.PLAYER_START_CLS
        self.items: dict[str, int] = {}

    def add_item(self, item: str, quantity: int = 1) -> None:
        """
        Adds an item to a Player's inventory.

        Parameters
        ----------
        item : str
            Item name.
        quantity : int, optional
            Item quantity, by default 1.
        """
        if item in self.items.keys():
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        print(f"Added {item} to inventory.")

    def remove_item(self, item: str) -> None:
        """
        Removes an item from a Player's inventory.

        Parameters
        ----------
        item : str
            Item name.
        """
        try:
            del self.items[item]
        except Exception:
            print(f"Could not remove {item} from inventory. It may already be removed.")

    def use_item(self, item: str) -> None:
        """
        If an item is available in the Player's inventory,
        uses that item.

        !!! warning
            Item effects not currently implemented.

        Parameters
        ----------
        item : str
            Item name.
        """
        if item in self.items.keys() and self.items[item] > 0:
            print(f"Used {item}.")
            self.items[item] -= 1
            if self.items[item] == 0:
                self.remove_item(item)
        else:
            print(f"No {item} in inventory to use!")

    def change_hp(self, hp_delta: int) -> None:
        """
        Change a Player's health points. `Player.hp` is bracketed by 0 and `Player.hp_max`.

        Parameters
        ----------
        hp_delta : int
            Change in health points.
            Can be positive or negative.
        """
        self.hp += hp_delta
        if self.hp > self.hp_max:
            self.hp = self.hp_max
        elif self.hp < 0:
            self.hp = 0

    def print_attacks(self, attack_dict: dict):
        if self.cls is not None:
            print("Attacks")
            print("-------")
            for req_level, attacks in attack_dict.items():
                if req_level <= self.level:
                    for attack in attacks:
                        print(f"- {attack}")


class _PlayerClass:
    def __init__(self) -> None:
        self.name: str = "Default Player Class"
        self.phy_attacks: dict[int, list[str]] = {}
        self.mag_attacks: dict[int, list[str]] = {}
        self.phy_damage: int = 1
        self.mag_damage: int = 2


class Wizard(_PlayerClass):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Wizard"
        self.phy_attacks = {
            test_game.PLAYER_START_LEVEL: ["Staff Bonk"],
            test_game.PLAYER_START_LEVEL + 1: ["Staff Smash"],
        }
        self.mag_attacks = {test_game.PLAYER_START_LEVEL: ["Fireball"], test_game.PLAYER_START_LEVEL + 1: ["Iceball"]}


class Thief(_PlayerClass):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Thief"


class Warrior(_PlayerClass):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Warrior"


if __name__ == "__main__":
    P1 = Player()
    P1.cls = Wizard()

    P1.print_attacks(P1.cls.phy_attacks)

    P1.level = 2

    P1.print_attacks(P1.cls.phy_attacks)
