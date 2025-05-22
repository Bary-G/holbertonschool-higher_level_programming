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
        self._size = None
        self.size = size

    @property
    def size(self):
        """
        Gets the size of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Verifies and sets the size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        Return the area of the square.
        """
        if not isinstance(self.size, int):
            raise TypeError("size must be an integer")
        elif self.size < 0:
            raise ValueError("size must be >= 0")
        return self.size * self.size

    def my_print(self):
        """
        Print the square with '#' character.
        """
        if not isinstance(self.size, int) or self.size == 0:
            print("")
        else:
            for _ in range(self.size):
                print("#" * self.size)
