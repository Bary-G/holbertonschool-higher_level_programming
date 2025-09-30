#!/usr/bin/python3
import json
"""
Module : A Python file that runs functions.
json : A Python module to convert into JSON.
"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    json_string = json.dumps(my_obj)
    return json_string
