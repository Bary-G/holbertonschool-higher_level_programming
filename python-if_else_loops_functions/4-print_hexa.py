#!/usr/bin/python3
"""Print hexadecimal value of a number"""
num = 0
while num <= 98:
    print(str.format(f"{num} = {hex(num)}"))
    num = num + 1
