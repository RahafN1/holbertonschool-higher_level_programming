#!/usr/bin/python3
"""Module that defines a function to insert a line of text after
each line containing a specific string in a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text to a file after each line containing
    search_string.
    """
    with open(filename, mode="r", encoding="UTF8") as f:
        lines = f.readlines()

    with open(filename, mode="w", encoding="UTF8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
