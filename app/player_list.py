from app.player_node import PlayerNode

class PlayerList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    #Checks if the head is empty or not
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    #Insert a node at the head
    def insert_at_head(self, player):
        new_node = PlayerNode(player)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head.previous = new_node
            self.__head = new_node
