#!/usr/bin/python3
"""
Module: A Python script file with functions.
"""


class Rectangle():
    """
    A class that defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        All privates instances.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self._Square__width = width
        self._Square__height = height

    @property
    def width(self):
        """
        A property to get the width
        """
        return self._Square__width

    @width.setter
    def width(self, value):
        """
        A property to define the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._Square__width = value

    @property
    def height(self):
        """
        A property to get the height
        """
        return self._Square__height

    @height.setter
    def height(self, value):
        """
        A property to define the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._Square__height = value
