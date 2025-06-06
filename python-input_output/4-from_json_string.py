#!/usr/bin/python3
import json
"""
Module:
A file that runs Python functions.
"""


def from_json_string(my_str):
    """
    A function that unserialize JSON data.
    """
    return json.loads(my_str)
