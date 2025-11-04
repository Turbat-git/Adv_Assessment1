from player import Player
from player_list import PlayerList
from player_hash_map import PlayerHashMap
from player_bst import PlayerBST
import random, math

if __name__ == "__main__":
    sorted_tree = []
    bst = PlayerBST()
    players = [Player(unique_id='01', player_name="Aline", score=10),
               Player(unique_id='02', player_name="Trial", score=5),
               Player(unique_id='03', player_name="Bline", score=7),
               Player(unique_id='04', player_name="Lama", score=20),
               Player(unique_id='05', player_name="Zombie", score=15), ]

    for p in players:
        bst.insert(p)

    sorted_list = bst.in_order_traversal(sorted_tree, bst.root)

    balanced_tree = bst.create_balanced_tree(sorted_list)
    print(balanced_tree.player.name, balanced_tree.player.uid)
    print(balanced_tree.right.player.name, balanced_tree.right.player.uid)
    print(balanced_tree.left.player.name, balanced_tree.left.player.uid)
    print(balanced_tree.left.right.player.name, balanced_tree.left.right.player.uid)

    print(bst.root.player.name)
    print(bst.root.right.player.name)
    print(bst.root.left.player.name)

    print(bst.search('Aline'))

    # print(sorted_tree)
    # print(sorted_list)
    #
    # print(5//2)
    # print(sorted_list[2])
    # print(sorted_list[:2])
    # print(sorted_list[3:])
    