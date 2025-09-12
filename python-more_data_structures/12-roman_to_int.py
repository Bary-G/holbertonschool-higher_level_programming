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
    prev_num = 0
    converted_num = 0
    for prev_num in range(len(roman_string) -1):
        for key, value in roman_dict.items():
            if roman_string[prev_num] == key:
                if prev_num < converted_num:
                    converted_num -= value
                else:
                    converted_num += value
    return converted_num
