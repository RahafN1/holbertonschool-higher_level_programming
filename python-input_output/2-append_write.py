#!/usr/bin/python3
"""Module that defines a function to append a string to a text file."""


def append_write(filename="", text=""):
    """Append a string to a text file (UTF8) and return chars added."""
    with open(filename, mode="a", encoding="UTF8") as f:
        return f.write(text)
