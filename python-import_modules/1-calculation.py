#!/usr/bin/python3
from calculator_1 import *
"""Calculate 2 values by importing functions from another file"""
if __name__ == "__main__":
    a = 10
    b = 5
    print(str.format(f"{a} + {b} = {add(a, b)}"))
    print(str.format(f"{a} - {b} = {sub(a, b)}"))
    print(str.format(f"{a} * {b} = {mul(a, b)}"))
    print(str.format(f"{a} / {b} = {div(a, b)}"))
