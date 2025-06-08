#!/usr/bin/python3
import json
"""
Module:
A file that runs Python functions.
"""


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it.
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def load_and_deserialize(filename):
    """
    Load data and deserialize it.
    """
    with open(filename, 'r') as file:
        return json.load(file)
