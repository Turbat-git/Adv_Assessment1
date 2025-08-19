from player import Player


class PlayerNode:
    def __init__(self, player):
        self._player = player
        self._prev_node = None
        self._next_node = None

    @property
    def player(self) -> Player:
        return self._player

    @property
    def get_next(self):
        return self._next_node

    @property
    def get_previous(self):
        return self._prev_node

    def set_next(self, node):
        self._next_node = node

    def set_previous(self, node):
        self._prev_node = node

    @property
    def key(self):
        return self.player.uid

    def __str__(self):
        return (f"Current player is {self.player}. Player id: {self.key}. Next node is {self.get_next} and previous "
                f"node is {self.get_previous}")

