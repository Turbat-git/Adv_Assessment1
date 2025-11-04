from player import Player
from player_list import PlayerList
from player_hash_map import PlayerHashMap
from player_bst import PlayerBST
import random, math

if __name__ == "__main__":
    sorted_tree = []
    bst = PlayerBST()
    players = [Player(unique_id='01', player_name="Aline", score=10),
               Player(unique_id='02', player_name="Alice", score=5),
               Player(unique_id='03', player_name="Bline", score=7),
               Player(unique_id='04', player_name="Alice", score=20),
               Player(unique_id='05', player_name="Alice", score=15), ]

    for p in players:
        bst.insert(p)

    sorted_list = bst.in_order_traversal(sorted_tree, bst.root)
    print(sorted_list)

    balanced_tree = bst.create_balanced_tree(sorted_list)
    print(balanced_tree)

    