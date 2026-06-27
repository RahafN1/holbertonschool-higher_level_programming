#!/usr/bin/python3
"""Module that defines MyInt class inheriting from int"""


class MyInt(int):
    """A rebel class that inverts == and != operators"""

    def __eq__(self, other):
        """Inverts == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts != operator"""
        return super().__eq__(other)
