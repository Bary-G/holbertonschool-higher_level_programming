#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Show a matrix"""
    for i in matrix:
        for j in i:
            print(str.format(f"{"{:d}".format(j)}"), end=" ")
        print()
