#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace element in a new list"""
    new_list = my_list[:]
    if not isinstance(idx, int):
        return new_list
    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list[idx] = element
    return new_list
