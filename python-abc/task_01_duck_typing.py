from abc import ABC, abstractmethod
import math
"""
Module: all modules docstrings
abc: Abstract Base Classes module
ABC: Abstract Base Classes package
math: used to calculate circle area and perimeter
"""


class Shape(ABC):
    """Class that represents Shape"""
    def area(self):
        """Shape area"""
        pass

    def perimeter(self):
        """Shape perimeter"""
        pass


class Circle(Shape):
    """Class that represents Circle"""
    def __init__(self, radius):
        """Class init"""
        self.__radius = radius

    def area(self):
        """Shape area"""
        return math.pi * self.__radius ** 2

    def perimeter(self):
        """Shape perimeter"""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Class that represents Rectangle"""
    def __init__(self, width, height):
        """Class init"""
        self.__width = width
        self.__height = height

    def area(self):
        """Shape area"""
        return self.__width * self.__height

    def perimeter(self):
        """Shape perimeter"""
        return self.__width + self.__height * 2


def shape_info(shape):
    """Displays area and perimeter using duck typing"""
    print(f"Aire : {shape.area()}")
    print(f"Périmètre : {shape.perimeter()}")
