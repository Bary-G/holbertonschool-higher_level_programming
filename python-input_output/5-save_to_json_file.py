#!/usr/bin/python3
"""
Module : A Python file that tuns functions.
json : A Python module to convert into JSON.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation
    """
    with open(filename, 'w', encoding='UTF8') as file:
        count = file.write(json.dumps(my_obj))
    return count
