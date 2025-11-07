import unittest
from player_bst import PlayerBST
from player import Player
import random

class TestPlayerBSTSearch(unittest.TestCase):
    def setUp(self):
        self.bst = PlayerBST()
        self.bst.insert(Player('1',"Alice", 100))
        self.bst.insert(Player('2', "Bob", 150))
        self.bst.insert(Player('3', "Charlie", 200))

    def test_search_found(self):
        """Test searching for a player that exists in the tree."""

        result = self.bst.search("Alice")
        self.assertEqual(result.name, "Alice")
        self.assertEqual(result.score, 100)

        result = self.bst.search("Bob")
        self.assertEqual(result.name, "Bob")
        self.assertEqual(result.score, 150)

        result = self.bst.search("Charlie")
        self.assertEqual(result.name, "Charlie")
        self.assertEqual(result.score, 200)

    def test_search_not_found(self):
        """Test searching for a player that does not exist in the tree."""

        result = self.bst.search("David")
        self.assertIsNone(result)

    def test_search_empty_tree(self):
        """Test searching in an empty tree."""

        empty_bst = PlayerBST()
        result = empty_bst.search("Alice")
        self.assertIsNone(result)

    def test_search_case_sensitivity(self):
        """Test that search is case-sensitive."""

        self.bst.insert(Player("4","alice", 100))

        result = self.bst.search("alice")
        self.assertEqual(result.unique_id, "4")

        result2 = self.bst.search("Alice")
        self.assertNotEqual(result2.unique_id, "4")
        self.assertEqual(result2.unique_id, "1")

if __name__ == '__main__':
    TestPlayerBSTSearch()