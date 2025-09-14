#!/usr/bin/python3
"""
Module: A Python script file with functions.
"""


def print_square(size):
    """
    A function that prints a square with the character #.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
