#!/usr/bin/python3
def max_integer(my_list=[]):
    """Find the biggest int of a list"""
    max_int = None
    if not my_list:
        return max_int
    elif isinstance(my_list[0], int):
        max_int = my_list[0]
    for i in my_list:
        if isinstance(i, int) and i > max_int:
            max_int = i
    return max_int
