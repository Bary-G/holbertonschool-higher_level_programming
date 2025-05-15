#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace a variable in a list"""
    if not isinstance(idx, int):
        return my_list
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
