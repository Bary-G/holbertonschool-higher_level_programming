#!/usr/bin/python3

def print_last_digit(number):
    """
    A function that displays the last digit of a number.
    """
    if number >= 0:
        lastdigit = number % 10
    else:
        lastdigit = abs(number) % 10
    print(lastdigit, end="")
    return lastdigit
