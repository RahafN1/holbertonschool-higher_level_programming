#!/usr/bin/python3
"""Module that defines Animal abstract class and its subclasses"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class Animal with abstract method sound"""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses"""
        pass


class Dog(Animal):
    """Dog class that inherits from Animal"""

    def sound(self):
        """Returns the sound a dog makes"""
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal"""

    def sound(self):
        """Returns the sound a cat makes"""
        return "Meow"
