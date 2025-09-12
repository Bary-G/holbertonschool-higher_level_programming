#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    A function that prints x elements of a list.
    """
    count = 0
    try:
        for item in my_list:
            if count < x:
                print("{}".format(item), end="")
                count += 1
        print("")
        return count
    except TypeError:
        return count
