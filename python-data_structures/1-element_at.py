#!/usr/bin/python3
def element_at(my_list, idx):
    """Index a variable in a list"""
    if not isinstance(idx, int):
        return None
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
