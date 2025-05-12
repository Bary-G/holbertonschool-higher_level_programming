#!/usr/bin/python3
"""Show numbers from 0 to 99"""
num = 0
while num <= 99:
    print(str.format(f"{num:02}"), end="")
    if num != 99:
        print(str.format(f", "), end="")
    num = num + 1