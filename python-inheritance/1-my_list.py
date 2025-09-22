#!/usr/bin/python3
"""
Module: A python Script that runs functions.
"""


class MyList(list):
    """A simple class named MyList"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        for obj in self:
            if not isinstance(obj, int):
                raise TypeError("list must contain only integers")
        print(sorted(self))
