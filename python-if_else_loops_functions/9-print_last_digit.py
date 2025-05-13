#!/usr/bin/python3
def print_last_digit(number):
    """Return last digit"""
    last_digit = abs(number) % 10
    print(str.format(f"{last_digit}"), end="")
    return last_digit
