#!/usr/bin/python3
"""Print text with 2 new lines after '.', '?' and ':'"""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?' and ':'"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_space = False

    for char in text:
        if skip_space and char == " ":
            continue

        skip_space = False
        print(char, end="")

        if char in ".?:":
            print("\n", end="")
            skip_space = True
