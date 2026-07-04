#!/usr/bin/python3
"""Module that defines a function to save an Object to a text file
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Write an Object to a text file, using a JSON representation."""
    with open(filename, mode="w", encoding="UTF8") as f:
        json.dump(my_obj, f)
