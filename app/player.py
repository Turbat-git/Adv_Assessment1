import random
from typing import MutableSequence

class Player:
    def __init__(self, unique_id: str, player_name: str, score: int = 0):
        """
        Initialize a Player Object

        :param unique_id: Unique ID of the player
        :param player_name: Name of the player
        :param score: Score of the player
        """
        self.unique_id = unique_id
        self.player_name = player_name
        self._score = score

    @property
    def uid(self):
        """Getter function for the unique id param"""
        return self.unique_id

    @property
    def name(self):
        """Getter function for the player name param"""
        return self.player_name

    @property
    def score(self):
        """Getter function for the score param"""
        return self._score

    @score.setter
    def score(self, score: int):
        """Setter function for the score param"""
        if isinstance(score, int):
            self._score = score
        else:
            raise TypeError("The score must be a positive value!")

    def __str__(self) -> str:
        return f"Player's name is {self.name} and ID: {self.uid}"

    @classmethod
    def pearson_hash(cls,
                     key: str,
                     table_size: int = 256) -> int:
        """
        Computes the Pearson Hash of a player's unique ID

        :param key: Take in the player's unique ID
        :param table_size: Size of the pearson hash function's table is used for hashing
        :return: Hash value of the player's unique ID
        """
        hash_value = 0
        lookup_table = list(range(table_size))

        for char in key:
            hash_value = lookup_table[hash_value ^ ord(char)]
        return hash_value % table_size

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

    def __repr__(self):
        """Function to return the player object's details."""
        return f"{self.__class__.__name__}(name={self.name!r}, uid={self.uid!r}, score={self._score})\n"

    def __lt__(self, other) -> bool:
        """Function to compare if the score of the player is less than another player's"""
        if self._score < other._score:
            return True
        else:
            return False

    def __gt__(self, other) -> bool:
        """Function to compare if the score of the player is greater than another player's"""
        if self._score > other._score:
            return True
        else:
            return False

    @classmethod
    def sort_quickly(cls, player_list: MutableSequence) -> MutableSequence:
        """
            Simple sort function that will return a list with a sorted values that are descending in order.

            :param player_list: A list with int values within it.
            :return: Sorted List with values that are descending.
        """
        if len(player_list) <= 1:
            return player_list
        n = random.randint(0, len(player_list) - 1)
        pivot = player_list.pop(n)
        left = []
        right = []
        for x in player_list:
            if x > pivot:
                left.append(x)
            else:
                right.append(x)
        return cls.sort_quickly(left) + [pivot] + cls.sort_quickly(right)

