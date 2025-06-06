#!/usr/bin/python3
"""
Module:
A file that runs Python functions.
"""
import json


def to_json_string(my_obj):
    """
    A function that serialize Python data.
    """
    return json.dumps(my_obj)
