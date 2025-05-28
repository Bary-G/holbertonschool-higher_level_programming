#!/usr/bin/python3
"""
Module:
A Python script that contains the inherits_from function.
"""


def inherits_from(obj, a_class):

    """
    A function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class,
    otherwise False.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
