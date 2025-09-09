#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    A function that adds 2 tuples.
    """
    if tuple_a == None:
        result_a = (0, 0)
    elif len(tuple_a) < 2:
        result_a = tuple_a + (0,) * (2 - len(tuple_a))
    elif len(tuple_a) > 2:
        result_a = (tuple_a[0], tuple_a[1])
    else:
        result_a = tuple_a
    if tuple_b == None:
        result_b = (0, 0)
    elif len(tuple_b) < 2:
        result_b = tuple_b + (0,) * (2 - len(tuple_b))
    elif len(tuple_b) > 2:
        result_b = (tuple_b[0], tuple_b[1])
    else:
        result_b = tuple_b
    return (result_a[0] + result_a[1], result_b[0] + result_b[1])
