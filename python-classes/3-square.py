#!/usr/bin/python3
"""
Module:
A Square class that represents... a square.
"""


class Square:
    """
    Represents a square shape with attributes and methods to define its
    properties.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def _Square__size(self):
        """
        Gets the size of the square.
        """
        return self._size

    def _Square__size(self, value):
        """
        Sets the size of the square with basic validation.
        """
        if not isinstance(value, int) or value < 0:
            raise ValueError
        self._size = value

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size * self.__size
