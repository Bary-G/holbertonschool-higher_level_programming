#!/usr/bin/python3
"""
Module: A python Script that runs functions.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class ;
    otherwise False.
    """
    if obj is None or a_class is None:
        return False
    return isinstance(obj, a_class)
