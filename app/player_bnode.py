class PlayerBNode:
    def __init__(self, player):
        self._player = player
        self._right = None
        self._left = None

    @property
    def player(self):
        return self._player

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left