#!/usr/bin/python3
"""
Module : A Python file that tuns functions.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, 'a', encoding='UTF8') as file:
        count = file.write(text)
    return count
