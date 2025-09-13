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

    def __getitem__(self, key: str) -> Player | None:
        """
        Returns the Player object for the given ID. None if the ID doesn't exist.

        :param key: Player's unique ID.
        :return: Player object. None if the ID doesn't exist.'
        """
        #Get the player's appropriate PlayerList
        player_list = self.hashmap[self.get_index(key)]

        current = player_list.head

        #If exists, get the Player Object
        while current:
            if current.key == key:
                return current.player
            current = current.next

        #If player doesn't exist return None
        return None


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

    def __delitem__(self, key: str) -> Player | None:
        """
        Finds the Player object with the given ID and deletes it.

        :param key: Player's unique ID.
        :return: None.
        """
        player_list = self.hashmap[self.get_index(key)]

        removed_player = player_list.delete_by_key(key)

        if removed_player is None:
            print("Player Not Found.")
            return None

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
