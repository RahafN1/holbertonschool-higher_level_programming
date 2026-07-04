#!/usr/bin/env python3
"""Module that defines a function to convert CSV data to JSON
format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Read data from a CSV file and write it as JSON to data.json.

    Args:
        csv_filename: The filename of the input CSV file.

    Returns:
        True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, mode="r", encoding="UTF8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", mode="w", encoding="UTF8") as json_file:
            json.dump(data, json_file)

        return True
    except Exception:
        return False
