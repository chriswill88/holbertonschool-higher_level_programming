#!/usr/bin/python3
"""
modual function count lines
"""


def read_lines(filename="", nb_lines=0):
    """
    function read_lines -
    reads up to nb_lines lines
    """
    i = 0
    with open(filename) as f:
        for line in f:
            i += 1
            print(line, end="")
            if i == nb_lines:
                return i
    return i
