#!/usr/bin/python3
"""Show numbers from 0 to 99"""
num = 0
while num <= 99:
    if num != 99:
        print(str.format(f"{num:02}"), end=", ")
    else:
        print(str.format(f"{num:02}"))
    num = num + 1