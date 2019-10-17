#!/usr/bin/python3
"""
modual function count lines
"""


def number_of_lines(filename=""):
    """
    function number_of_lines -
    counts and returns lines.
    """
    i = 0
    with open(filename) as f:
        for line in f:
            i += 1
    return i
