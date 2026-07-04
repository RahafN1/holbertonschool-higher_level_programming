#!/usr/bin/python3
"""Module that defines a function to return an object represented
by a JSON string.
"""
import json


def from_json_string(my_str):
    """Return an object (Python data structure) from a JSON string."""
    return json.loads(my_str)
