#!/usr/bin/python3
"""
Module:
A Rectangle class that represents a rectangular shape.
"""


class Rectangle:
    """
    Represents a rectangular shape with attributes and methods to define its
    properties.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with a given size.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle.
        """
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle with basic validation.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.
        """
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle with basic validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value

    def area(self):
        """
        Return the rectangle area.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the rectangle perimeter.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
