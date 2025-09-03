#!/usr/bin/python3

def uppercase(str):
    """
    A function that displays a string in uppercase followed by a new line.
    """
    newcharacter = ""
    linereturn = "\n"
    for character in str:
        if ord(character) >= 97 and ord(character) <= 122:
            newcharacter = chr(ord(character) - 32)
        else:
            newcharacter = character
        print("{}".format(newcharacter), end="")
    print("{}".format(linereturn), end="")
