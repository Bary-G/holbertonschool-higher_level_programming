#!/usr/bin/python3
def roman_to_int(roman_string):
    """converts a Roman numeral to an integer"""
    if not isinstance(roman_string, str) or roman_string == None:
        return None

    number