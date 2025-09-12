#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    Function:
        Converts a Roman numeral to an integer.
    Args:
        roman_string: The Roman numeral to convert (str).
    Return:
        Converted Roman numeral (int).
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dict = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    prev_value = 0
    converted_num = 0
    for char in reversed(roman_string):
        value = roman_dict.get(char, 0)
        if value < prev_value:
            converted_num -= value
        else:
            converted_num += value
        prev_value = value
    return converted_num
