#!/usr/bin/python3
"""
This program returns a list of all available attrributes and methods of an object
"""


def lookup(obj):
    """
    lookup: returns a list of available attributes and methods of an objects

    its passed in an obj

    returns a list of attributes and methods
    """
    return dir(obj)
