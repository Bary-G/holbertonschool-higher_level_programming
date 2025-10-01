#!/usr/bin/python3
"""
Module : A Python file that tuns functions.
json : A Python module to convert into JSON.
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file
    """
    with open(filename, 'r', encoding='UTF8') as file:
        object = json.load(file)
    return object
