#!/usr/bin/python3
"""Module that defines MyList class inheriting from list"""


class MyList(list):
    """Class that inherits from list with a print_sorted method"""

    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        print(sorted(self)) 
