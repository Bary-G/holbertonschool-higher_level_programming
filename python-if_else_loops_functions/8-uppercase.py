#!/usr/bin/python3
def uppercase(str):
    """Show texting in uppercase"""
    result = ""
    for i in str:
        if 'a' <= i <= 'z':
            result += chr(ord(i) - 32)
        else:
            result += i
    print(format(f"{result}"))
