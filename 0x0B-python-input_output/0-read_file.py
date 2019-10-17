#!/usr/bin/python3
"""
modual function reads a text file prints to stdout
"""


def read_file(filename=""):
    """
    function read_file - 
    reads file using with and open.
    """
    with open(filename, 'r') as f:
        for line in f:
            print(line)
