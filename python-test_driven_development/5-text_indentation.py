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

    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"

    lines = result.split("\n")
    output = "\n".join(line.strip() for line in lines)
    while output.endswith("\n"):
        output = output[:-1]
    print(output)
