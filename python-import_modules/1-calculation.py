#!/usr/bin/python3
import __main__
from calculator_1 import *
"""Add 2 values by importing function from another file"""
a = 15
b = 5
print(str.format(f"{a} + {b} = {add(a, b)}"))
print(str.format(f"{a} - {b} = {sub(a, b)}"))
print(str.format(f"{a} * {b} = {mul(a, b)}"))
print(str.format(f"{a} / {b} = {div(a, b)}"))
