from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList

if __name__ == "__main__":
    p1 = Player("1234", "Trial Person")
    p2 = Player("1235", "Person Trial")
    p3 = Player("1236", "Person Person")

    plist = PlayerList()

    plist.insert_at_head(p1)
    plist.insert_at_head(p2)
    plist.insert_at_head(p3)

    PlayerList.display(plist, forward=False)
    PlayerList.display(plist, forward=True)