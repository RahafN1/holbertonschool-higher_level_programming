#!/usr/bin/python3
"""This module defines a Square class with getter and setter"""


class Square:
    """A class that defines a square by its size"""

    def __init__(self, size=0):
        """Initialize a new Square instance
        Args:
            size (int): the size of the square, defaults to 0
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square
        Returns:
            int: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square
        Args:
            value (int): the new size of the square
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square
        Returns:
            int: the area of the square
        """
        return self.__size ** 2
