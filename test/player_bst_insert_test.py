import unittest
from player_bst import PlayerBST
from player import Player
import random

class TestPlayerBSTInsert(unittest.TestCase):
    def test_insert_into_empty_tree(self):
        """Test inserting the first player creates the root node."""
        self.bst = PlayerBST()
        player = Player("1234", "Trial Person", 0)
        self.bst.insert(player)

        self.assertEqual(self.bst.root.player.name, "Trial Person")
        self.assertEqual(self.bst.root.player.score, 0)
        self.assertIsNone(self.bst.root.left)
        self.assertIsNone(self.bst.root.right)

    def test_insert_left_and_right_nodes(self):
        """Test that inserting players alphabetically left/right builds BST correctly."""
        self.bst = PlayerBST()
        players = [Player(unique_id='01', player_name="Bob", score=10),
                   Player(unique_id='02', player_name="Alice", score=5),
                   Player(unique_id='03', player_name="Charlie", score=15)]

        for p in players:
            self.bst.insert(p)

        self.assertEqual(self.bst.root.player.name, "Bob")
        self.assertEqual(self.bst.root.left.player.name, "Alice")
        self.assertEqual(self.bst.root.right.player.name, "Charlie")

    def test_insert_multiple_levels(self):
        """Test inserting players forms deeper tree correctly."""
        self.bst = PlayerBST()
        players = [Player(unique_id='01', player_name="Bob", score=10),
                   Player(unique_id='02', player_name="Alice", score=5),
                   Player(unique_id='03', player_name="Charlie", score=7),
                   Player(unique_id='04', player_name="Bane", score=20),
                   Player(unique_id='05', player_name="Doe", score=15),]

        for p in players:
            self.bst.insert(p)

        self.assertEqual(self.bst.root.left.player.name, "Alice")
        self.assertEqual(self.bst.root.right.player.name, "Charlie")
        self.assertEqual(self.bst.root.left.right.player.name, "Bane")
        self.assertEqual(self.bst.root.right.right.player.name, "Doe")

    def test_insert_duplicate_updates_player(self):
        """Test that inserting a duplicate player name updates existing node."""
        self.bst = PlayerBST()
        player1 = Player("1", "Mina", 10)
        player2 = Player("1", "Mina", 19)

        self.bst.insert(player1)
        self.bst.insert(player2)

        self.assertEqual(self.bst.root.player.score, 19)
        self.assertIsNone(self.bst.root.left)
        self.assertIsNone(self.bst.root.right)

    def test_sorting_unbalanced_tree(self):

        sorted_tree = []
        self.bst = PlayerBST()
        players = [Player(unique_id='01', player_name="Bob", score=10),
                   Player(unique_id='02', player_name="Alice", score=5),
                   Player(unique_id='03', player_name="Charlie", score=7),
                   Player(unique_id='04', player_name="Bane", score=20),
                   Player(unique_id='05', player_name="Doe", score=15), ]

        for p in players:
            self.bst.insert(p)

        self.bst.in_order_traversal(sorted_tree)


if __name__ == "__main__":
    TestPlayerBSTInsert()