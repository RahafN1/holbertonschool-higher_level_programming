#!/usr/bin/python3
"""This module defines a Node and SinglyLinkedList class"""


class Node:
    """A class that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a new Node instance
        Args:
            data (int): the data of the node
            next_node (Node): the next node, defaults to None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list"""

    def __init__(self):
        """Initialize a new SinglyLinkedList instance"""
        self.__head = None

    def __str__(self):
        """Print the entire list"""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """Insert a new Node in the correct sorted position
        Args:
            value (int): the value to insert
        """
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None:
            if value < current.next_node.data:
                new_node.next_node = current.next_node
                current.next_node = new_node
                return
            current = current.next_node

        current.next_node = new_node
