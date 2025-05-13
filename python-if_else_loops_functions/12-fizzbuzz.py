#!/usr/bin/python3
def fizzbuzz():
    """Print Fizz if multiple of 3, Buzz if multiple of 5, number otherwise"""
    i = 0
    while i < 100:
        i = i + 1
        if i % 3 == 0 and i % 5 == 0:
            print(str.format(f"FizzBuzz"), end=" ")
        elif i % 3 == 0:
            print(str.format(f"Fizz"), end=" ")
        elif i % 5 == 0:
            print(str.format(f"Buzz"), end=" ")
        else:
            print(str.format(f"{i}"), end=" ")
