#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    A function that replaces or adds key/value in a dictionary.
    """
    if not isinstance(key, str) or value is None:
        return a_dictionary
    a_dictionary[key] = value
    return a_dictionary
