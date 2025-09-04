#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    last_chars = ""
    if len(argv) == 1:
        last_chars = "s."
    elif len(argv) == 2:
        last_chars = ":"
    else:
        last_chars = "s:"
    print("{} argument{}".format(len(argv) - 1, last_chars))
    if len(argv) > 1:
        for index in range(len(argv) - 1):
            print("{}: {}".format(index + 1, argv[index + 1]))
