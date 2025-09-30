#!/usr/bin/python3
import json
"""
Module : A Python file that runs functions.
json : A Python module to convert data.
"""


def to_json_string(my_obj):
    """Returns the converted representation of an object (string)"""
    return json.dumps(my_obj)
