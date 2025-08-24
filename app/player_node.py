from app.player import Player


class PlayerNode:
    def __init__(self, player):
        self.__player = player
        self.__prev_node = None
        self.__next_node = None

    @property
    def player(self):
        return self.__player

    @property
    def next(self):
        return self.__next_node

    @property
    def previous(self):
        return self.__prev_node

    @next.setter
    def next(self, node):
        self.__next_node = node

    @previous.setter
    def previous(self, node):
        self.__prev_node = node

    @property
    def key(self):
        return self.player.uid

    def __str__(self):
        return (f"Current player is {self.player}. Player id: {self.key}. Next node is {self.next} and previous "
                f"node is {self.previous}")

