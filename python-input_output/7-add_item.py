#!/usr/bin/python3
"""
Module : A Python file that runs functions.
json : A Python module to use JSON objects.
sys : A Python module to import arguments.
os : A Python module to browse OS files.
"""
import json
import sys
import os

FILENAME = "add_item.json"


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def main():
    """Main configuration of main module"""
    data = load_from_json_file(FILENAME)
    data.extend(sys.argv[1:])
    save_to_json_file(data, FILENAME)


if __name__ == "__main__":
    main()
