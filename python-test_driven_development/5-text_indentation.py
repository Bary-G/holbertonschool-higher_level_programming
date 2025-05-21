#!/usr/bin/python3
"""
Module:
Test cases for the text_indentation function
"""


def text_indentation(text):
    """Print text with two new lines after '.', '?', and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
        i += 1

    lines = result.split("\n")
    for line in lines:
        print(line.strip())
