#!/usr/bin/python3
"""Show numbers from 0 to 99"""
num = 0
while num <= 99:
    if num < 10:
        print(str.format("0"), end="")
    print(str.format(f"{num}"), end=", ")
    num = num + 1
