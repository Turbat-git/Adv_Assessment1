import unittest
from app.player import Player
from app.player_list import PlayerList

class TestPlayerList(unittest.TestCase):
    def setUp(self):
        self.p1 = Player("1234", "Trial Person")
        self.p2 = Player("1235", "Person Trial")
        self.p3 = Player("1236", "Person Person")

    def test_insert_at_head_empty_list(self):
        plist = PlayerList()
        plist.insert_at_head(self.p1)

        self.assertFalse(plist.is_empty())
        self.assertEqual(plist.head.player, self.p1)

    def test_insert_at_head_non_empty_list(self):
        plist = PlayerList()

        plist.insert_at_head(self.p1)
        plist.insert_at_head(self.p2)
        plist.insert_at_head(self.p3)

        self.assertEqual(plist.head.player, self.p3)
        self.assertEqual(plist.head.next.player, self.p2)
        self.assertEqual(plist.tail.player, self.p1)
        self.assertIsNone(plist.tail.next)

    def test_insert_at_tail_empty(self):
        plist = PlayerList()

        plist.insert_at_tail(self.p1)

        self.assertEqual(plist.head.player, self.p1)
        self.assertEqual(plist.tail.player, self.p1)
        self.assertIsNone(plist.tail.next)

    def test_insert_at_tail_multiple(self):
        plist = PlayerList()

        plist.insert_at_tail(self.p1)
        plist.insert_at_tail(self.p2)
        plist.insert_at_tail(self.p3)

        self.assertEqual(plist.tail.player, self.p3)
        self.assertEqual(plist.tail.previous.player, self.p2)
        self.assertIsNone(plist.tail.next)

if __name__ == '__main__':
    unittest.main()