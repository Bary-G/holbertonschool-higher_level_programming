#!/usr/bin/python3
"""
Module:
A Python script that contains Rectangle class,
that inherits from BaseGeometry class.
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


class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle, inheriting from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangle with validated width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def my_print(self):
        """
        Print the rectangle with print_symbol character.
        """
        if not isinstance(self.width, int) or self.width == 0:
            print("")
            return
        elif not isinstance(self.height, int) or self.height == 0:
            print("")
            return
        for _ in range(self.height):
            print(str(self.print_symbol) * self.width)

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def my_print(self):
        """
        Print the square with '#' character.
        """
        if self.size == 0:
            print("")
            return

        print("\n" * self.position[1], end="")

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
