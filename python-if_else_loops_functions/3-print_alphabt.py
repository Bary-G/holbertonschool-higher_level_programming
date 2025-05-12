#!/usr/bin/python3
"""Return ASCII alphabet without q and e"""
i = 97
while i <= 122:
    if i != 101 and i != 113:
        print(str.format(chr(i)), end="")
    i = i + 1
