from player import Player
import unittest
from unittest import TestCase


class TestPlayer(unittest.TestCase):
    def test_uid(self):
        player = Player("1234", "Trial Person")
        self.assertEqual(player.unique_id, "1234")

    def test_name(self):
        player = Player("1234", "Trial Person")
        self.assertEqual(player.player_name, "Trial Person")

    def test_hash_function(self):
        player = Player("test123", "Test Person")
        h = hash(player)

        self.assertIsInstance(h, int)
        self.assertTrue(0 <= h <= 255)


if __name__ == "__main__":
    TestPlayer()