#!/usr/bin/python3
"""
Module : A Python file that runs functions.
json : A Python module to convert into JSON.
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
