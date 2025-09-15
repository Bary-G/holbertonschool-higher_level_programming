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

    def area(self):
        """
        A public instance method that returns the current square area
        """
        return self._Square__size ** 2
