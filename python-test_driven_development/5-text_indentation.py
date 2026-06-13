#!/usr/bin/python3
"""
Module that prints text with 2 new lines after ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each ., ? and :

    Args:
        text: the text to print

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    n = len(text)
    i = 0
    for char in text:
        print(char, end="")
        if char in ".?:" and i + 1 < n:
            print("\n")
        i += 1
