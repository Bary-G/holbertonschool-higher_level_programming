#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Show list integer"""
    i = 0
    while i < len(my_list):
        print(str.format(f"{my_list[i]}"))
        i = i + 1
