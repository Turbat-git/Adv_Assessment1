import unittest
from player_hash_map import PlayerHashMap

class TestPlayerList(unittest.TestCase):
    def setUp(self):
        self.hash_map = PlayerHashMap()

        self.hash_map.set("1234", "Trial Person")
        self.hash_map.set("1235", "Person Trial")
        self.hash_map.set("1236", "Person Person")
        self.hash_map.set("1237", "Person Person")

    def test_add_player(self):
        self.hash_map.set("1239", "Trial Person")

        player = self.hash_map.get("1239")

        self.assertEqual(player.name, "Trial Person")

    def test_update_player(self):
        self.hash_map.set("1234", "New Name")
        player = self.hash_map.get("1234")

        self.assertEqual(player.name, "New Name")

    def test_remove_player(self):
        self.hash_map.remove("1234")

        self.assertIsNone(self.hash_map.get("1234"))

    def test_check_size(self):
        size = self.hash_map.size()

        self.assertEqual(size, 4)

    def test_get_index(self):
        index1 = self.hash_map.get_index("1234")
        index2 = self.hash_map.get_index("1235")

        self.assertEqual(index1, 4)
        self.assertEqual(index2, 5)

    def test_collision_handling(self):
        self.hash_map.set("1234", "Trial Person")
        self.hash_map.set("4321", "Person Trial")

        player1 = self.hash_map.get("1234")
        player2 = self.hash_map.get("4321")

        self.assertEqual(player1.name, "Trial Person")
        self.assertEqual(player2.name, "Person Trial")

if __name__ == '__main__':
    unittest.main()