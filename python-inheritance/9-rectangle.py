#!/usr/bin/python3
"""
Module: A python Script that runs functions.
"""


class BaseGeometry:
    """A simple geometry base class."""

    def area(self):
        """Raises an exception if not implemented in subclass."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if value is an integer:
            if value is not an integer: raises a TypeError exception,
            with the message <name> must be an integer
            if value is less or equal to 0: raises a ValueError exception
            with the message <name> must be greater than 0
        """
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Class Instantiation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description"""
        return f"[Rectangle] {self.__width}/{self.__height}"
