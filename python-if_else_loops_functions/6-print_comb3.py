#!/usr/bin/python3
"""Show possible combinations of 2 digits"""
for i in range(10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print(str.format(f"{i}{j}"), end="\n")
        else:
            print(str.format(f"{i}{j}"), end=", ")
