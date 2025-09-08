#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    A function that replaces an element in a list at a specific position
    without modifying the original list.
    """
    new_list = my_list[:]
    if idx > len(new_list) - 1 or idx < 0:
        return new_list
    else:
        new_list[idx] = element
        return new_list
