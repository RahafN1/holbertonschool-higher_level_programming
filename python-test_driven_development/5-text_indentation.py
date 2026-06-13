#!/usr/bin/python3
"""
This module provides a function that prints text with 2 new lines
after each of these characters: . ? and :
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?' or ':'.
    Raises TypeError if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
