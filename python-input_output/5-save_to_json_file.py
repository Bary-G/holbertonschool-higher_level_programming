#!/usr/bin/python3
import json
"""
Module:
A file that runs Python functions.
"""


def save_to_json_file(my_obj, filename):
    """
    A function that writes an Object to a text file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(my_obj, file, indent=4)
        return file
    except Exception as e:
        raise TypeError("Object of type set is not JSON serializable")
