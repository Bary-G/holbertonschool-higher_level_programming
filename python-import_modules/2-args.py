#!/usr/bin/python3
import sys
"""Show a list of arguments"""
if __name__ == "__main__":
    i = 0
    args = sys.argv[1:]
    print(str.format(f"{len(args)} argument"), end="")
    if len(args) == 0:
        print(str.format(f"s."))
    else:
        if len(args) > 1:
            print(str.format(f"s"), end="")
        print(str.format(f":"))
        while i < len(args):
            i = i + 1
            print(str.format(f"{i}: {args[i - 1]}"))
