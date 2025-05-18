#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list"""
    multiple_of_2_list = []
    if not my_list:
        return multiple_of_2_list
    for i in my_list:
        if isinstance(i, int) and i % 2 == 0:
            multiple_of_2_list = multiple_of_2_list + [i]
    return multiple_of_2_list
