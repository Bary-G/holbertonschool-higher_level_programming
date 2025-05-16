#!/usr/bin/python3
def max_integer(my_list=[]):
    """Find the biggest int of a list"""
    if not my_list and not isinstance(my_list[0], int):
        return None
    max_int = my_list[0]
    for i in my_list:
        if i > max_int and isinstance(i, int):
            max_int = i
    return max_int
