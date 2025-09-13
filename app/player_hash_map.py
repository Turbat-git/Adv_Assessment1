import random
from app.player import Player
from app.player_list import PlayerList


class PlayerHashMap:
    """
    A hash map to store Player Objects.
    """

    # A constant for the size
    SIZE: int = 10

    def __init__(self):
        """
        Initialize a hash map.
        """
        self.hashmap = [PlayerList() for _ in range(self.SIZE)]

    def get_index(self, key: str | Player) -> int:
        """
        Get the index of the given key.

        :param key: Player's unique ID.
        :return: The index of where the key should be stored in the hash table.
        """
        if isinstance(key, Player):
            return hash(key) % self.SIZE
        else:
            return Player.pearson_hash(key, 256) % self.SIZE

    def __getitem__(self) -> Player | None:
        pass

    def __setitem__(self, key: str, name: str) -> None:
        """
        Add a new Player or update the existing Player's name in the hash table.

        :param key: Player's unique ID.
        :param name: Player's name
        """
        # get the player's appropriate PlayerList:
        player_list = self.hashmap[self.get_index(key)]

        # check if the player is in the list
        current = player_list.head

        # If it is, update the player's name
        while current:
            if current.key == key:
                current.player.player_name = name  # Update the name
                return
            current = current.next

        # If it isn't, create a player and add the player to the player list
        new_player = Player(key, name)
        player_list.insert_at_tail(new_player)

    def display(self):
        pass