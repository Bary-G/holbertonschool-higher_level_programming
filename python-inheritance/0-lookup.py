#!/usr/bin/python3
"""
Module:
A Python script that contain the lookup function.
"""

def lookup(obj):
    """
    A function that returns the list of available attributes
    and methods of an object.
    """
    return (dir(obj))
    