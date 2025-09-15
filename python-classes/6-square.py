#!/usr/bin/python3
"""
Module: A Python script file with functions.
"""


class Square():
    """
    A class that defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        All privates instances.
        """
        pos_err_ty = "position must be a tuple of 2 positive integers"
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if (not isinstance(position, tuple) or len(position) != 2 or
            not all(isinstance(i, int) and i >= 0 for i in position)):
            raise TypeError(pos_err_ty)
        self._Square__size = size
        self._Square__position = position

    @property
    def size(self):
        """
        A property to get the size
        """
        return self._Square__size

    @property
    def position(self):
        """
        A property to get the position
        """
        return self._Square__position

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

    @position.setter
    def position(self, value):
        """
        A property to define the position
        """
        pos_err_ty = "position must be a tuple of 2 positive integers"
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError(pos_err_ty)
        self._Square__position = value

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
            return
        lines = [" " * self._Square__position[0] + "#" * self._Square__size
                for _ in range(self._Square__size)]
        print("\n" * self._Square__position[1] + "\n".join(lines))