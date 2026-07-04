#!/usr/bin/env python3
"""Module that defines basic serialization and deserialization
functions using JSON.
"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to JSON and save it to a file.

    Args:
        data: A Python dictionary with data to serialize.
        filename: The filename of the output JSON file. If it
            already exists, it will be replaced.
    """
    with open(filename, mode="w", encoding="UTF8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize JSON data from a file.

    Args:
        filename: The filename of the input JSON file.

    Returns:
        A Python dictionary with the deserialized JSON data.
    """
    with open(filename, mode="r", encoding="UTF8") as f:
        return json.load(f)
