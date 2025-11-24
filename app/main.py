from player import Player
from player_list import PlayerList
from player_hash_map import PlayerHashMap
import random

if __name__ == "__main__":
    p1 = Player("1234", "Trial Person")
    p2 = Player("1235", "Person Trial")
    p3 = Player("1236", "Person Person")

    players = [Player(player_name=f"Player {i}",
                      unique_id=f"{i:03}",
                      score=random.randint(0, 1000)) for i in range(1000)]

    sorted_players = Player.sort_players_desc(players)
    # print(f"{repr(sorted_players)}\n")
    print(repr(sorted_players))

