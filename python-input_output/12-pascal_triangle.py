#!/usr/bin/python3
"""
Module:
A file that runs Python functions.
"""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n."""
    if not isinstance(n, int):
        raise TypeError("'n' must be an int")
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
