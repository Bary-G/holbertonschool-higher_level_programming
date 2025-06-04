#!/usr/bin/python3
"""
Module:
A file that runs Python functions.
"""


def write_file(filename="", text=""):
    """
    A function that write in a text file.
    """
    try:
        with open(filename, "r"):
            pass
    except FileNotFoundError:
        with open(filename, "w"):
            pass

    with open(filename, "a") as f:
        f.write(text)
        return len(text)
