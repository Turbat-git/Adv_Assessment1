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

    @root.setter
    def root(self, root):
        """
        Setter function for the root of the BST
        """
        self._root = root

    def insert(self, player: Player, node: PlayerBNode = None):
        """
        Inserts a player into the tree based on the player's score

        :param player: Player object
        :param node: Points to the specific node in the BST
        """
        if self.root is None:
            self.root = PlayerBNode(player)

        if node is None:
            node = self.root

        if player.uid == node.player.uid:
            if player.score > node.player.score:
                node.player = player

        elif player.name < node.player.name or player.name == node.player.name:
            if node.left is None:
                node.left = PlayerBNode(player)
            else:
                self.insert(player, node.left)

        elif player.name > node.player.name:
            if node.right is None:
                node.right = PlayerBNode(player)
            else:
                self.insert(player, node.right)

    def search(self, name: str, node: PlayerBNode = None) -> Player | None:
        """
        Search for a player by name

        :param name: Name of the player
        :param node: Points to the specific node in the BST
        :return: Player or None
        """
        if node is None:
            node = self.root
            if node is None:
                return None

        if name == node.player.name:
            return node.player

        elif name < node.player.name:
            if node.left is None:
                return None
            else:
                return self.search(name, node.left)

        elif name > node.player.name:
            if node.right is None:
                return None
            else:
                return self.search(name, node.right)

    def in_order_traversal(self, array: list, node: PlayerBNode) -> list[Player] | None:
        """
        Sorts the binary search tree

        :param array: to be used for adding the values of the nodes
        :param node: Points to the specific node in the BST
        :return: List full of the player's names
        """
        if node:
            self.in_order_traversal(array, node.left)

            array.append(node.player)

            self.in_order_traversal(array, node.right)

        return array

    def create_balanced_tree(self, sorted_list: list[Player]):
        """
        Use a sorted list to create a balanced tree

        :param sorted_list: List of players that have been sorted
        :return: root
        """
        if len(sorted_list) == 0:
            return None

        middle = len(sorted_list) // 2
        node = PlayerBNode(sorted_list[middle])

        node.left = self.create_balanced_tree(sorted_list[:middle])
        node.right = self.create_balanced_tree(sorted_list[middle + 1:])

        return node

