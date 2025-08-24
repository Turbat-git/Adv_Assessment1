import unittest
from app.player import Player
from app.player_list import PlayerList

class TestPlayerList(unittest.TestCase):

    def test_insert_at_head_empty_list(self):
        plist = PlayerList()
        player = Player("1234", "Trial Person")
        plist.insert_at_head(player)

        self.assertFalse(plist.is_empty())
        self.assertEqual(plist.head.player, player)

    def test_insert_at_head_non_empty_list(self):
        plist = PlayerList()
        p1 = Player("1234", "Trial Person")
        p2 = Player("4321", "Person Trial")

        plist.insert_at_head(p1)
        plist.insert_at_head(p2)

        self.assertEqual(plist.head.player, p2)
        self.assertEqual(plist.head.next.player, p1)
        self.assertEqual(plist.head.next.previous.player, p2)

if __name__ == '__main__':
    unittest.main()