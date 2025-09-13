from player_node import PlayerNode

class PlayerList:
    """
    A doubly linked list that contains nodes PlayerNode objects.

    Attributes:
    """
    def __init__(self):
        self._head = None
        self._tail = None

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def is_empty(self):
        """
        Checks if the list is empty.

        :return: Boolean indicating if the list is empty.
        """
        if self.head is None:
            return True
        else:
            return False

    def insert_at_head(self, player):
        """
        Inserts a player at the head node.

        :param player: Adds a player object to the head node of the list.
        """
        new_node = PlayerNode(player)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.previous = new_node
            self._head = new_node

    def insert_at_tail(self, player):
        """
        Inserts a player at the tail node.

        :param player: Takes in a Player object to add at tail node of the list
        """
        new_node = PlayerNode(player)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.previous = self._tail
            self._tail.next = new_node
            self._tail = new_node

    def delete_head(self):
        """
        Remove and return the Player object at the head node.

        :return: Player object of the removed head node.
        """
        if self.is_empty():
            raise IndexError('The list is empty')
        removed_node = self._head
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            self._head = self._head.next
            self._head.previous = None
        return removed_node.player

    def delete_tail(self):
        """
        Remove and return the Player object at the tail node.

        :return: Player object of the removed tail node.
        """
        if self.is_empty():
            raise IndexError('The list is empty')
        removed_node = self._tail
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            self._tail = self._tail.previous
            self._tail.next = None
        return removed_node.player

    def delete_by_key(self, key):
        """
        Remove a node by the Player's unique ID.

        :param key: Player's unique ID
        :return: Player Object of the removed node or None if no node was found.
        """
        current = self._head
        while current is not None:
            if current.key == key:
                if current == self._head:
                    return self.delete_head()
                elif current == self._tail:
                    return self.delete_tail()
                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                    return current.player
            current = current.next
        raise IndexError('The Player with this ID does not exist')

    def display(self, forward=True):
        """
        Print the list of Player objects.

        :param forward: Boolean value to determine whether to print from head to tail. If True, Forward. Else, Backwards.
        :return: Printed list
        """
        if self.is_empty():
            raise IndexError('The list is empty')

        if forward:
            current = self._head
            print("Displaying list from head to tail:")
            while current:
                print(current.player)
                current = current.next
        else:
            current = self._tail
            print("Displaying list from tail to head:")
            while current:
                print(current.player)
                current = current.previous
