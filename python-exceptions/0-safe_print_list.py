#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints number of elements from a list"""
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
        print()
    except Exception as e:
        print()
    return count
