from app.player import Player
import unittest
from unittest import TestCase


class TestPlayer(unittest.TestCase):
    def test_uid(self):
        player = Player("1234", "Trial Person")
        self.assertEqual(player.unique_id, "1234")

    def test_name(self):
        player = Player("1234", "Trial Person")
        self.assertEqual(player.player_name, "Trial Person")


if __name__ == "__main__":
    TestPlayer()