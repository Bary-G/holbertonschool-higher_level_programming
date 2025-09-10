#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    A function that deletes a key in a dictionary.
    """
    if key is None or key == "" or not isinstance(key, str):
        return a_dictionary
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
