#!/usr/bin/python3
"""This module defines a Square class with size validation"""


class Square:
    """A class that defines a square by its size"""

    def __init__(self, size=0):
        """Initialize a new Square instance
        Args:
            size (int): the size of the square, defaults to 0
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
