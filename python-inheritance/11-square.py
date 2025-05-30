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

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    A class that represents a square, inheriting from Rectangle class.
    """
    def __init__(self, size):
        """
        Initializes a square with validated size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Computes and returns the area of the square.
        """
        return self.__size * self.__size

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

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
