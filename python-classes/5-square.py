#!/usr/bin/python3
"""
Module: A Python script file with functions.
"""


class Square():
    """
    A class that defines a square.
    """
    def __init__(self, size=0):
        """
        All privates instances.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    @property
    def size(self):
        """
        A property to get the size
        """
        return self._Square__size

    @size.setter
    def size(self, value):
        """
        A property to define the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        """
        A public instance method that returns the current square area
        """
        return self._Square__size ** 2

    def my_print(self):
        """
        A public instance method that prints in stdout the square
        with the character #
        """
        if self._Square__size == 0:
            print("")
        for _ in range(self._Square__size):
            print("#" * self._Square__size)
