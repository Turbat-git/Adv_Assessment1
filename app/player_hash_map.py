from player import Player
from player_list import PlayerList


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

        :param key: Player's unique ID or the Player class.
        :return: The index of where the key should be stored in the hash table.
        """
        if isinstance(key, Player):
            return hash(key) % self.SIZE
        elif isinstance(key, str):
            return Player.pearson_hash(key) % self.SIZE
        else:
            raise TypeError("Value entered must either be Player or a Player's unique ID")

    def __getitem__(self, key: str) -> Player:
        """
        Returns the Player object for the given ID. Raises exception if the ID doesn't exist.

        :param key: Player's unique ID.
        :return: Player object. Raises exception if the ID doesn't exist.
        """
        # Get the player's appropriate PlayerList
        player_list = self.hashmap[self.get_index(key)]

        player = player_list.find(key)
        if player is None:
            raise KeyError(f"{key} doesn't exist!")
        return player

    def __setitem__(self, key: str, name: str) -> None:
        """
        Add a new Player or update the existing Player's name in the hash table.

        :param key: Player's unique ID.
        :param name: Player's name
        """
        # get the player's appropriate PlayerList:
        player_list = self.hashmap[self.get_index(key)]

        player = player_list.find(key)

        if player:
            player.player_name = name
        else:
            # If player doesn't exist, create a player and add the player to the player list
            new_player = Player(key, name)
            player_list.insert_at_tail(new_player)

    def __len__(self) -> int:
        """
        Return the number of Player objects in the hash table.

        :return: Integer. Count of the Player objects.
        """

        count = 0

        for player_list in self.hashmap:
            current = player_list.head
            while current:
                count += 1
                current = current.next
        return count

    def __delitem__(self, key: str) -> Player:
        """
        Finds the Player object with the given ID and deletes it.

        :param key: Player's unique ID.
        :return: None.
        """
        player_list = self.hashmap[self.get_index(key)]

        removed_player = player_list.delete_by_key(key)

        if removed_player is None:
            print("Player Not Found.")
            raise KeyError(f"{key} doesn't exist!")

        return removed_player

    def remove(self, key: str) -> None:
        """Removes a player from the hash table using the given ID."""
        self.__delitem__(key)

    def size(self) -> int:
        """Return the number of Player objects in the hash table."""
        return self.__len__()

    def get(self, key: str) -> Player | None:
        """Returns the Player object for the given ID. None if the ID doesn't exist."""
        return self.__getitem__(key)

    def set(self, key: str, name: str) -> None:
        """Add a new Player or update the existing Player's name in the hash table."""
        return self.__setitem__(key, name)

    def display(self) -> None:
        """
        Prints the index of the PlayerList and the players in the list
        """
        for index, player_list in enumerate(self.hashmap):
            if not player_list.is_empty():
                print(index)
                player_list.display(True)
