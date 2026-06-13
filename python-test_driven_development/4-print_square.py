#!/usr/bin/python3
"""
Module that prints a square with the character #.
"""


def print_square(size):
    """
    Prints a square of # with side length size.

    Args:
        size: side length of the square, must be an integer >= 0

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
