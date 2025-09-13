from typing import AnyStr

class Player:
    def __init__(self, unique_id: AnyStr, player_name: AnyStr):
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
                     key: str,
                     table_size: int) -> int:
        hash_ = 0
        lookup_table = list(range(table_size))

        for char in key:
            hash_ = lookup_table[hash_ ^ ord(char)]
        return hash_ % size

    def __hash__(self):
        return self.pearson_hash(self.uid, 256)