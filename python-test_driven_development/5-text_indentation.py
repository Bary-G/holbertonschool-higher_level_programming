#!/usr/bin/python3
"""
Module: A Python script file with functions.
"""


def text_indentation(text):
    """
    A function that prints a text with 2 new lines after each of these
    characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    chars = ".?:"
    result = ""

    for c in text:
        result += c
        if c in chars:
            result += "\n\n"
    print(result)
