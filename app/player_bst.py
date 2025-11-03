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
        :param _node: To be used for recursion
        :return:
        """
        if self._root is None:
            self._root = PlayerBNode(player)
            return self._root

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

    def search(self, player: Player):
        pass