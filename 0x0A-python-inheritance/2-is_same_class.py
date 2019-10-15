#!/usr/bin/python3
"""
This modual contains the program is_same_class
"""


def is_same_class(obj, a_class):
    """
    is _same_class - checks if obj is of a_class

    Parameters:
        obj - the object
        a_class - the class

    Returns:
        True if obj is of a_class
        or False if not
    """
    if type(obj) is a_class:
        return True
    return False
