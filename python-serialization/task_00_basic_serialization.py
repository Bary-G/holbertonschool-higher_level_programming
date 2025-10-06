#!/usr/bin/env python3
"""
Module : A Python file that runs functions.
json : A module to convert data
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return json.dump(data, file)

def load_and_deserialize(filename):
    """
    Deserialize a JSON file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
