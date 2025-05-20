#!/usr/bin/python3

"""
Module:
This module throws 2 integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    This function takes two arguments, a and b, and returns their sum as an
    integer. If a or b are floats, they are converted to integers before
    performing the addition.
    
    Args:
        a (int, float): The first number. Must be an integer or a float.
        b (int, float, optional): The second number. Defaults to 98.
        Must be an integer or a float.

    Returns:
        int: The sum of a and b after converting any float inputs to integers.

    Raises:
        TypeError: If `a` or `b` is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
