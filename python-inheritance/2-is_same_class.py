#!/usr/bin/python3
"""
Module:
A Python script that contains the is_same_class function.
"""


def is_same_class(obj, a_class):

    """
    A function that returns True of obj is exactly an instance of the
    specified class from list, False otherwise.
    """
    return type(obj) is a_class
