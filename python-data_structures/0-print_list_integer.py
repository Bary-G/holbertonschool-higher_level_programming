#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Prints each integer in the list on a new line using str.format()"""
    for i in my_list:
        print("{:d}".format(i))
