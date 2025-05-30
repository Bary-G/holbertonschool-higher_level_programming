#!/usr/bin/python3
"""
Module:
A Python script that contains the BaseGeometry class.
"""


class BaseGeometry:
    """
    A class that represents a geometric base.
    """
    def area(self):
        """
        A method that raises an Exception with a message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is an integer and greater than 0.
        """
        if not isinstance(name, str):
            raise TypeError(f"{name} must be a string")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
