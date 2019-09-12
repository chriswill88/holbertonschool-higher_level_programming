#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    dot = ":"
    plural = "arguments"
    argc = len(argv) - 1

    if argc == 0:
        dot = "."
    if argc == 1:
        plural = "argument"

    print("{} {}{}".format(argc, plural, dot))

    if argc > 0:
        for i in range(1, argc + 1):
            print("{}: {}".format(i, argv[i]))
            i += 1
