#!/usr/bin/python3
from abc import ABC, abstractmethod
import math

"""
Module:
A script that contains abstract classes.
"""


class Shape(ABC):
    """
    An abstract class that represents a shape.
    """

    @abstractmethod
    def area(self):
        """
        Return the area.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Return the perimeter.
        """
        pass


class Circle(Shape):
    """
    Represents a circle from Shape abstract class.
    """

    def __init__(self, radius=0):
        """
        Initializes the circle with a given radius.
        """
        if not isinstance(radius, (int, float)) or radius < 0:
            raise ValueError("Radius must be a non-negative number")
        self.radius = radius

    def area(self):
        """
        Return the area of the circle.
        """
        return math.pi * self.radius * self.radius

    def perimeter(self):
        """
        Return the perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Represents a rectangle from Shape abstract class.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with a given size.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Return the area of the circle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter (circumference) of the circle.
        """
        return (self.width + self.height) * 2


def shape_info(Shape):
    """
    Pass the shape info.
    """
    try:
        print("Area:", Shape.area())
        print("Perimeter:", Shape.perimeter())
    except AttributeError:
        raise Exception
