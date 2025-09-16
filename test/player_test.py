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

    def test_sort_players(self):
        players = [Player(unique_id='01', player_name="Alice", score=10),
                   Player(unique_id='02', player_name="Bob", score=5),
                   Player(unique_id='03', player_name="Charlie", score=15)]
        # note: ensure initialization code is valid for **your** implementation.
        # For example, is your parameter called uid? is the first parameter name?

        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player(unique_id='02', player_name="Bob", score=5),
                                   Player(unique_id='01', player_name="Alice", score=10),
                                   Player(unique_id='03', player_name="Charlie", score=15)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        # note: ensure initialization code is valid for **your** implementation
        alice = Player(player_name="Alice", unique_id='01', score=10)
        bob = Player(player_name="Bob", unique_id='02', score=5)

        # Add the appropriate expression to the following assert test
        self.assertTrue(bob < alice)
        # or, event better
        self.assertLess(alice, bob)


if __name__ == "__main__":
    TestPlayer()
