#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    A function that prints all integers of a list, in reverse order.
    """
    for index in my_list:
        print("{:d}".format(my_list[len(my_list) - index]))
