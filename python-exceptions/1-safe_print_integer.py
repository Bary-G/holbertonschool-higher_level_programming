#!/usr/bin/python3
def safe_print_integer(value):
    """Prints number of elements from a list"""
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        return False
