#!/usr/bin/python3
"""Print numbers from 0 to 99"""
num = 0
while num <= 99:
    if num < 10:
        print(format("0"), end="")
    print(format(num), end=", ")
    num = num + 1
