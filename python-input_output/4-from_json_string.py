#!/usr/bin/python3
"""
Module:
A file that runs Python functions.
"""
import json


def from_json_string(my_str):
    """
    A function that unserialize JSON data.
    """
    return json.loads(my_str)
