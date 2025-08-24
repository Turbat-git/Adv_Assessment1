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

    #Insert a node at the head
    def insert_at_tail(self, player):
        new_node = PlayerNode(player)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.previous = self.__tail
            self.__tail.next = new_node
            self.__tail = new_node

    #Delete a node that's at the head
    def delete_head(self):
        if self.is_empty():
            return None
        removed_node = self.__head
        if self.__head == self.__tail:
            self.__head = self.__tail = None
        else:
            self.__head = self.__head.next
            self.__head.previous = None
        return removed_node.player

    #Delete a node that's at the tail
    def delete_tail(self):
        if self.is_empty():
            return None
        removed_node = self.__tail
        if self.__head == self.__tail:
            self.__head = self.__tail = None
        else:
            self.__tail = self.__tail.previous
            self.__tail.next = None
        return removed_node.player

    #Delete a node through key, and return None result if not found
    def delete_by_key(self, key):
        current = self.__head
        while current is not None:
            if current.key == key:
                if current == self.__head:
                    return self.delete_head()
                elif current == self.__tail:
                    return self.delete_tail()
                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                    return current.player
            current = current.next
        return None