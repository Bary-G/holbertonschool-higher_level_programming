#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    A function that prints a matrix of integers.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            last_chr = " "
            if j == len(matrix[i]) - 1:
                last_chr = ""
            print("{:d}".format(matrix[i][j]), end=last_chr)
        print("{:d}".format("\n"), end="")
