#!/usr/bin/python3
"""
Module:
Test cases for the matrix_divided function
"""
def matrix_divided(matrix, div):
    """Divides all matrix elements"""
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise ValueError("matrix must be a non-empty matrix (list of non-empty lists)")
    row_lengths = {len(row) for row in matrix}
    if len(row_lengths) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in row] for row in matrix]
