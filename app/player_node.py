from player import Player


class PlayerNode:
    """
    A node in a doubly linked list that has a Player object.
    """
    def __init__(self, player: Player):
        """
        Initialize PlayerNode object

        :param player: Player object within the node
        """
        self._player = player
        self._prev_node = None
        self._next_node = None

    @property
    def player(self) -> Player | None:
        return self._player

    @property
    def next(self):
        return self._next_node

    @property
    def previous(self):
        return self._prev_node

    @next.setter
    def next(self, node):
        self._next_node = node

    @previous.setter
    def previous(self, node):
        self._prev_node = node

    @property
    def key(self) -> str:
        return self.player.uid

    def __str__(self):
        return (f"Current player is {self.player}. Player id: {self.key}. Next node is {self.next} and previous "
                f"node is {self.previous}")
