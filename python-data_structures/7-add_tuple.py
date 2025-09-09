#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    A function that adds 2 tuples.
    """
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    result_a = (tuple_a[0] + tuple_b[0])
    result_b = (tuple_a[1] + tuple_b[1])
    return (result_a, result_b)
