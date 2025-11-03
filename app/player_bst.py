from logging import raiseExceptions

from player import Player
from player_bnode import PlayerBNode

class PlayerBST:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        """
        Getter function for the root of the BST
        """
        return self._root

    def insert(self, player: Player, _node=None):
        """
        Inserts a player into the tree based on the player's score

        :param player: Player object
        :param _node: Points to the specific node in the BST
        """
        if self._root is None:
            self._root = PlayerBNode(player)

        if _node is None:
            _node = self._root

        if player.name == _node.player.name:
            if player.score > _node.player.score:
                _node.player = player

        elif player.name < _node.player.name:
            if _node.left is None:
                _node.left = PlayerBNode(player)
            else:
                self.insert(player, _node.left)

        elif player.name > _node.player.name:
            if _node.right is None:
                _node.right = PlayerBNode(player)
            else:
                self.insert(player, _node.right)

    def search(self, name: str, _node=None) -> Player|None:
        """
        Search for a player by name

        :param name: Name of the player
        :param _node: Points to the specific node in the BST
        :return: Player or None
        """
        if _node is None:
            _node = self._root
            if _node is None:
                return None

        if name == _node.player.name:
            return _node.player

        elif name < _node.player.name:
            if _node.left is None:
                return None
            else:
                return self.search(name, _node.left)

        elif name > _node.player.name:
            if _node.right is None:
                return None
            else:
                return self.search(name, _node.right)
