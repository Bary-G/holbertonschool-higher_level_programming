#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    A function that finds all multiples of 2 in a list.
    """
    new_list = my_list[:]
    if not my_list:
        return None
    for index in range(len(my_list)):
        if isinstance(my_list[index], int) and my_list[index] % 2 == 0:
            new_list[index] = True
        else:
            new_list[index] = False
    return new_list
