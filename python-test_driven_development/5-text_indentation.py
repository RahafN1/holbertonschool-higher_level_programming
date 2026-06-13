#!/usr/bin/python3
"""Module that prints text with 2 new lines after '.', '?' and ':'"""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?' and ':'"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = True

    for char in text:
        if char == " " and new_line:
            continue

        print(char, end="")

        if char in ".?:":
            print("\n", end="")
            new_line = True
        else:
            new_line = False
