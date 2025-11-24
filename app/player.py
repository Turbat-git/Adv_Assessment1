import random


class Player:

    _TABLE = list(range(256))
    random.shuffle(_TABLE)

    def __init__(self, unique_id: str, player_name: str):
        """
        Initialize a Player Object

        :param unique_id: Unique ID of the player
        :param player_name: Name of the player
        """
        self.unique_id = unique_id
        self.player_name = player_name

    @property
    def uid(self):
        return self.unique_id

    @property
    def name(self):
        return self.player_name

    def __str__(self) -> str:
        return f"Player's name is {self.name} and ID: {self.uid}"

    @classmethod
    def pearson_hash(cls,
                     key: str) -> int:
        """
        Computes the Pearson Hash of a player's unique ID

        :param key: Take in the player's unique ID
        :return: Hash value of the player's unique ID
        """
        hash_value = 0

        for char in key:
            hash_value = cls._TABLE[hash_value ^ ord(char)]
        return hash_value

    def __hash__(self) -> int:
        """
        Returns the hash value using the pearson hash function not the python hash function

        :return: Hash of the player's unique ID.
        """
        return self.pearson_hash(self.uid)

    def __eq__(self, other) -> bool:
        """
        Checks if two players' IDs are equal

        :param other: Another Player object
        :return: Boolean. If the unique IDs are same, True is returned.
        """
        return self.uid == other.uid
