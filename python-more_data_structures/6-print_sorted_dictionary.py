#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    A function that prints a dictionary by ordered keys.
    """
    sorted_dict = {key: a_dictionary[key] for key in sorted(a_dictionary)}
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")
