#!/usr/bin/python3
"""
Module: A python Script that runs functions.
"""


def is_kind_of_class(obj, a_class):
    """
    if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified
    class ; otherwise False.
    """
    if obj is None or a_class is None:
        return False
    return isinstance(obj, a_class)
