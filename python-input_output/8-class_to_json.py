#!/usr/bin/python3
"""
Module:
A file that runs Python functions.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of an object for JSON
    serialization.
    """
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    return {}
