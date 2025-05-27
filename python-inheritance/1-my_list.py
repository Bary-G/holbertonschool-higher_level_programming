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
        print(sorted(self))
