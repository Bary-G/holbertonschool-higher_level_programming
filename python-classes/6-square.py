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

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with a given size.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Gets the position of the square.
        """
        return self._position
    
    @position.setter
    def position(self, value):
        """
        Verifies and sets the position of the square.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or 
            not all(isinstance(x, int) and x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """
        Return the area of the square.
        """
        return self.size * self.size

    def my_print(self):
        """
        Print the square with '#' character.
        """
        if self.size == 0:
            print("")
            return

        print("\n" * self.position[1], end="")  # Vertical spacing

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)  # Horizontal spacing
