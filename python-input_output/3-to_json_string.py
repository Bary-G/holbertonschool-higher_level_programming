#!/usr/bin/python3
import json
"""
Module:
A file that runs Python functions.
"""


def to_json_string(my_obj):
    """
    A function that return a Python data structure into JSON string.
    """
    if not my_obj:
        return None
    return json.dumps(my_obj)
