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

    i = 0
    for char in text:
        if char in ".?:" and i + 1 < len(text):
            print(char)
            print()
        else:
            print(char, end="")
        i += 1
    print()
