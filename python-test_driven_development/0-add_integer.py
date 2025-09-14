#!/usr/bin/python3

def add_integer(a, b=98):
    """
    A function that adds 2 integers.
    
    Parameters:
    a: int or float - First number to add
    b: int or float - Second number to add (default is 98)

    Returns:
    int - The sum of a and b as integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
