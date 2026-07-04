#!/usr/bin/env python3
"""Module that defines a CustomObject class that can be serialized
and deserialized using the pickle module.
"""
import pickle


class CustomObject:
    """Represent a custom object with pickling support."""

    def __init__(self, name, age, is_student):
        """Initialize a new CustomObject.

        Args:
            name: A string representing the object's name.
            age: An integer representing the object's age.
            is_student: A boolean indicating if the object is a
                student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print out the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current instance and save it to a file.

        Args:
            filename: The filename to save the serialized object to.
        """
        try:
            with open(filename, mode="wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return an instance of CustomObject from a file.

        Args:
            filename: The filename to load the serialized object
                from.

        Returns:
            An instance of CustomObject, or None if the file doesn't
            exist or is malformed.
        """
        try:
            with open(filename, mode="rb") as f:
                return pickle.load(f)
        except Exception:
            return None
