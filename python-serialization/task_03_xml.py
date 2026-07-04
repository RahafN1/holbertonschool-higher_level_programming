#!/usr/bin/env python3
"""Module that defines functions to serialize and deserialize a
Python dictionary using XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary into XML and save it to a file.

    Args:
        dictionary: A Python dictionary to serialize.
        filename: The filename to save the XML data to.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Read XML data from a file and return a deserialized
    Python dictionary.

    Args:
        filename: The filename of the input XML file.

    Returns:
        A Python dictionary with the deserialized XML data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
