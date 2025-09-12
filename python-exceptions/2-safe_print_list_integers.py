#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    A function that display the first x elements of a list and only integers.
    """
    count = 0
    try:
        for item in my_list:
            if count < x and isinstance(item, int):
                print("{:d}".format(item), end="")
                count += 1
        print("")
        return count
    except IndexError:
        return count
