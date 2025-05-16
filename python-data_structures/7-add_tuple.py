#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Return the result of 2 added tuples"""
    if not all(isinstance(x, int) for x in tuple_a):
        return (0, 0)
    if not all(isinstance(x, int) for x in tuple_b):
        return (0, 0)
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
