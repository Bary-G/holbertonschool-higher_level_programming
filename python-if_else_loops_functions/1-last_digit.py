#!/usr/bin/python3
"""Print last digit"""
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
print(last_digit)