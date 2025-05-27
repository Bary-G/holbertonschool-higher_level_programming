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
        A method that sorts a list in ascending order.
        """
        if not all(isinstance(item, int) for item in self):
            raise TypeError("List contains non-integer elements")

        print(sorted(self))
        return sorted(self)
