from Node import Node


class LinkedList:

    def __init__(self) -> None:
        """
        Default constructor which will initialize a empty linked list
        """
        self.head = None
        self.count = 0

    def is_empty(self) -> bool:
        """
        This method return whether the list is empty or not.
        :return: bool
        """
        return self.count == 0

    def append(self, item) -> None:
        """
        This method will add a node at end of the list
        :param item: The integer value to add into the list
        """
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            self.count += 1
            return

        node = self.head
        while node.next != None:
            node = node.next
        node.next = new_node
        self.count = self.count+1

    def insert(self, position, item) -> None:
        """
        This method will add a node at given position. Position starts from 1.
        :param position: The integer pistion number where to add the value.
        :param item: The integer value to add into the list.
        """
        # invalid position
        if self.count+1 < position or position <= 0:
            print(f"Cannot add the node at that position. "
                  + f"Try another position between 1 to {self.count + 1}")
            return

        # position to add at the beginning or at the end
        if position == 1:
            self.insert_at_beginning(item)
            return
        elif position == self.count+1:
            self.append(item)
            return

        # postion at middle of the list
        new_node = Node(item)
        node = self.head
        temp = None
        for i in range(position-1):
            temp = node
            node = node.next
        temp.next = new_node
        new_node.next = node
        self.count += 1

    def insert_at_beginning(self, item) -> None:
        """
        This method will insert a node at the head.
        :params item: The integer value to add into the list.
        """
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def pop(self) -> int:
        """
        This method will delete the last node from the list.
        :return value: The deleted integer value.
        """
        if self.is_empty():
            print("List is empty.")
            return None

        node = self.head
        temp = None
        while node.next != None:
            temp = node
            node = node.next
        if temp != None:
            temp.next = None
        value = node.data
        del node
        self.count -= 1
        return value

    def remove(self, position) -> int:
        """
        This method will delte a node according to given position between 1 to number of elements.
        :param position: The integer position number.
        :return: The deleted integer value
        """
        # the list is empty
        if self.is_empty():
            print("List is empty.")
            return None
        # position indicate the first or last element of the list
        if position == 1:
            self.remove_at_beginning()
            return
        elif position == self.count:
            self.remove()
            return
        # position is in between
        node = self.head
        temp = None
        for i in range(position-1):
            temp = node
            node = node.next
        temp.next = node.next
        value = node.data
        del node
        self.count -= 1
        return value

    def remove_at_beginning(self) -> int:
        """
        This method will delete the first node from the list.
        :return: The deleted integer value.
        """
        if self.is_empty():
            print("List is empty.")
            return None

        node = self.head
        value = node.data
        self.head = self.head.next
        del node
        self.count -= 1
        return value

    def find(self, item) -> bool:
        """
        This method will check the provided value is present in the list or not.
        :param item: The targeted integer value.
        :return: True if the value is found, otherwise False.
        """
        if self.is_empty():
            return False
        node = self.head
        while node != None:
            if node.data == item:
                return True
            node = node.next
        return False

    def search(self, position) -> int:
        """"
        This method will traverse the list and find out the value of the node of provided position.
        :param position: The integer position number (starts from 1) where to find the value.
        :return: The searched value.
        """
        if position > self.count:
            return None
        node = self.head
        count = 1
        while node != None:
            if count == position:
                return node.data
            node = node.next
            count += 1

        return None

    def __str__(self) -> str:
        """
        This method returns all the elements of the list and total emements count.
        :return: Details about the list.
        """
        if self.is_empty():
            return "List is empty."

        elements = "List: "
        node = self.head
        for i in range(self.count):
            if i == self.count-1:
                elements += str(node.data)
            else:
                elements += (str(node.data) + " -> ")
            node = node.next
        elements += f"\nTotal Elements: {self.count}"
        return elements

    def reverse(self) -> None:
        """
        This method will reverse the entire list.
        """
        current_node = self.head
        prev_node = None
        next_node = None

        while current_node != None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node
