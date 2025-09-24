#!/usr/bin/python3
"""
Module: A python Script that runs functions.
"""


class BaseGeometry:
    """A simple geometry base class."""

    def area(self):
        """Returns the area of the shape."""
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
