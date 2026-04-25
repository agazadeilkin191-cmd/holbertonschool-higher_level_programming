#!/usr/bin/python3
"""Classes for a singly linked list."""


class Node:
    """Class for a node."""

    def __init__(self, data, next_node=None):
        """Initialize a node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Return data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Return next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next_node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class for a singly linked list."""

    def __init__(self):
        """Initialize an empty linked list."""
        self.__head = None

    def __str__(self):
        """Return string representation of the list."""
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """Insert a new node in sorted order."""
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
