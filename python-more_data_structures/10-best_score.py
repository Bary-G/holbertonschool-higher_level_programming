#!/usr/bin/python3

def best_score(a_dictionary):
    """
    A function that returns a key with the biggest integer value.
    """
    if not a_dictionary:
        return None
    best_key = -100**100
    best_value = -100**100
    for key, value in a_dictionary.items():
        if value > best_value:
            best_value = value
            best_key = key
    return best_key
