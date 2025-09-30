#!/usr/bin/python3
"""
Module : A Python file that runs functions.
json : A Python module to convert into JSON.
"""
import json


def from_json_string(my_str):
    """Returns a Python data structure represented by a JSON string"""
    return json.loads(my_str)
