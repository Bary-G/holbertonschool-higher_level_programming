#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints each integer from the list in reverse using str.format()"""
    for i in reversed(my_list):
        print("{:d}".format(i))
