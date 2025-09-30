#!/usr/bin/python3
"""
Module : A Python file that tuns functions.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, 'w', encoding='UTF8') as file:
        count = file.write(text)
    return count
