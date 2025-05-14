#!/usr/bin/python3
import sys
"""Add all numbers from argument list"""
if __name__ == "__main__":
    if not sys.argv[1:]:
        print(str.format(f"0"))
    else:
        args = map(int, sys.argv[1:])
        print(str.format(f"{sum(args)}"))
