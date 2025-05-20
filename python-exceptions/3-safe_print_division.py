#!/usr/bin/python3
def safe_print_division(a, b):
    """Prints result of division of 2 integers"""
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
