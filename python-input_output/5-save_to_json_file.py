#!/usr/bin/python3
"""
Module:
A file that runs Python functions.
"""
import json


def save_to_json_file(my_obj, filename):
    """Creates an object from a JSON file."""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
