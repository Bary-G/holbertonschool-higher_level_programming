#!/usr/bin/python3
character = 97
while character < 123:
    if character != 113 and character != 101:
        print(str.format(chr(character)), end="")
    character = character + 1
