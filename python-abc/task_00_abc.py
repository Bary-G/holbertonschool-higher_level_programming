#!/usr/bin/python3
from abc import ABC, abstractmethod
"""
Module:
A script that contains abstract classes.
"""


class Animal(ABC):
    """
    Represents a global animal abstract class.
    """

    @abstractmethod
    def sound(self):
        """
        The sound of the animal.
        """
        print(str.format(self))


class Dog(Animal):
    """
    Represents a dog class that inherits from Animal abstract class.
    """

    def sound(self):
        """
        The sound of the animal.
        """
        return str.format("Bark")


class Cat(Animal):
    """
    Represents a cat class that inherits from Animal abstract class.
    """

    def sound(self):
        """
        The sound of the animal.
        """
        return str.format("Meow")
