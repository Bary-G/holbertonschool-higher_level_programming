#!/usr/bin/python3
"""
Module:
A file that runs Python functions.
"""


def read_file(filename=""):
    """
    A function that reads a text file.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
