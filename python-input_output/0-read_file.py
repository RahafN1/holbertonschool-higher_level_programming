#!/usr/bin/python3
"""Module that defines a function to read and print a text file."""


def read_file(filename=""):
    """Read a text file and print its content to stdout."""
    with open(filename, encoding="UTF8") as f:
        print(f.read(), end="")
