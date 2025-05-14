#!/usr/bin/python3
from add_0 import add
"""Calculate 2 values by importing functions from another file"""
if __name__ == "__main__":
    a = 1
    b = 2
    print(str.format(f"{a} + {b} = {add(a, b)}"))
