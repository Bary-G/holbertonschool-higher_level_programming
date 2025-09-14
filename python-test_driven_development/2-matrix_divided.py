#!/usr/bin/python3
"""
Module: A Python script file with functions.
"""


def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix.
    """
    count = 0
    prev_row = 0
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    for row in matrix:
        if count != 0 and len(row) != len(prev_row):
            raise TypeError("Each row of the matrix must have the same size")
        prev_row = row
        count += 1
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_mat = [[round(val / div, 2) for val in ligne] for ligne in matrix[:]]
    return new_mat
