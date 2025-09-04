#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    result = 0
    if len(argv) > 1:
        for index in range(len(argv) - 1):
            result = result + int(argv[index + 1])
    print(result)
