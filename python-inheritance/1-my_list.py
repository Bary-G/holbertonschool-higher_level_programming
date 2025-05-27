#!/usr/bin/python3
"""
Module:
A Python script that contains the MyList class.
"""


class MyList(list):
    """
    A class that inherits from list.
    """
    def print_sorted(self):
        """
        A method that sorts a list of integers in ascending order.
        """
        if not all(isinstance(item, int) for item in self):
            raise TypeError("All elements in the list must be of type int.")
        print(sorted(self))
