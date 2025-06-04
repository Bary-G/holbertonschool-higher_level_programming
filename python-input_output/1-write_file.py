#!/usr/bin/python3
"""
Module:
A file that runs Python functions.
"""


def write_file(filename="", text=""):
    """
    A function that write in a text file.
    """
    with open(filename, "a") as f:
        f.write(text)
        return len(text)
