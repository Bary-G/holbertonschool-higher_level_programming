#!/usr/bin/python3
"""
Module: A Python script file with functions.
"""


def add_integer(a, b=98):
    """
    A function that adds 2 integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
