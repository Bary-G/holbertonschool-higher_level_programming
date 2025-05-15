#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Prints each integer from the list using str.format()"""
    for i in my_list:
        print("{:d}".format(i))
