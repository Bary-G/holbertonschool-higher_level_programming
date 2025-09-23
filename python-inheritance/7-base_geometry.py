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
        if not isinstance(name, str):
            raise TypeError(f"name must be a string")
        if not isinstance(value, int):
            raise TypeError(f"{value} must be an integer")
        if value <= 0:
            raise ValueError(f"{value} must be greater than 0")
