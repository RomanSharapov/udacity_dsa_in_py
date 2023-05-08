#!/usr/bin/env python3


class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __str__(self):
        nodes = []
        for node in self:
            nodes.append(str(node.value))
        return " -> ".join(nodes)

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current_position = 1
        for node in self:
            if current_position == position:
                return node
            current_position += 1
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        if position == 1:
            new_element.next = self.head
            self.head = new_element
            return

        current_position = 1
        previous_element = None
        for node in self:
            if current_position == position:
                new_element.next = node
                previous_element.next = new_element
                return
            previous_element = node
            current_position += 1

        if position == current_position:
            self.append(new_element)
        else:
            raise IndexError(
                "Index out of bounds. Use append() method to add "
                "an element to the LinkedList instance"
            )

    def delete(self, value):
        """Delete the first node with a given value."""
        previous_element = None
        for node in self:
            if node.value == value:
                if previous_element:
                    previous_element.next = node.next
                else:
                    self.head = node.next
                return
