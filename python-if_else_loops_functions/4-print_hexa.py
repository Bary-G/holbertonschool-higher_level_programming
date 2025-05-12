#!/usr/bin/python3
"""Print hexadecimal value of a number"""
num = 0
while num <= 98:
    print(num, "=", format(hex(num)))
    num = num + 1
