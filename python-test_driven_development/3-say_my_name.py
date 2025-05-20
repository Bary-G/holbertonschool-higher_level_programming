#!/usr/bin/python3
"""
Module:
Test cases for the say_my_name function
"""
def say_my_name(first_name, last_name=""):
    """prints first name and last name"""
    if not isinstance(first_name, str):
        print(str.format(f"first_name must be a string"))
        raise TypeError
    if not isinstance(last_name, str):
        print(str.format(f"last_name must be a string"))
        raise TypeError
    print(str.format(f"My name is {first_name} {last_name}"))