#!/usr/bin/python3
def uppercase(text):
    """Show texting in uppercase"""
    result = ""
    for i in text:
        if 'a' <= i <= 'z':
            result += chr(ord(i) - 32)
        else:
            result += i
    print(str.format(f"{result}"))
