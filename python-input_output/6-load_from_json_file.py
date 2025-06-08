#!/usr/bin/python3
"""
Module:
A file that runs Python functions.
"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename, 'r', encoding='UTF8') as file:
        return json.load(file)
