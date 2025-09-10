#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    A function that returns a set of common elements in two sets.
    """
    new_list = []
    for item_1 in set_1:
        for item_2 in set_2:
            if item_1 == item_2:
                new_list.append(item_1)
    return new_list
