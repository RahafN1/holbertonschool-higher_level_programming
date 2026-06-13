#!/usr/bin/python3
"""
Module that prints text with 2 new lines after ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    n = len(text)
    i = 0
    while i < n:
        char = text[i]
        if char == " " and (i == 0 or text[i - 1] in ".?:"):
            i += 1
            continue
        print(char, end="")
        if char in ".?:" and i + 1 < n:
            print("\n", end="")
        i += 1
