#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    A function that prints all integers of a list.
    """
    for index in my_list:
        str = "{}"
        print(str.format(my_list[index - 1]))
