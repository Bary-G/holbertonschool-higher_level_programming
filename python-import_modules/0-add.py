#!/usr/bin/python3
"""Add 2 values by importing function from another file"""
from add_0 import add
a = 1
b = 2
print(str.format(f"{a} + {b} = {add(1, 2)}"))
