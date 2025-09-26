from abc import ABC, abstractmethod
"""
Module: all modules docstrings
abc: Abstract Base Classes module
ABC: Abstract Base Classes package
"""

class Animal(ABC):
    """A simple Animal class that uses ABC package."""

    TypeErrMSG = "Can't instantiate abstract class Animal with abstract method sound"

    @abstractmethod
    def sound(self):
        """Must be implemented by subclasses, otherwise will raises a TypeError."""
        pass


class Dog(Animal):
    """A Dog class that inherits from Animal class."""

    def sound(self):
        """The sound of the Dog."""
        return "Bark"


class Cat(Animal):
    """A Cat class that inherits from Animal class."""

    def sound(self):
        """The sound of the Cat."""
        return "Meow"
