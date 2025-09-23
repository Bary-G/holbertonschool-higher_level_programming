#!/usr/bin/python3
"""
Module: A python Script that runs functions.
"""


class BaseGeometry:
    """A simple geometry base class."""

    def area(self):
        """Returns the area of the shape."""
        raise Exception("area() is not implemented")
