#!/usr/bin/python3
"""Module that defines a LockedClass with restricted instance attributes."""


class LockedClass:
    """Class that prevents dynamic creation of new instance attributes,
    except for 'first_name'.
    """
    __slots__ = ['first_name']
