#!/usr/bin/python3
"""
This modual contains the program is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class -
    checks if obj is of a_class or if obj inherits from a_class

    Parameters:
        obj - the object
        a_class - the class

    Returns:
        True if obj is of a_class
        or False if not
    """
    return isinstance(obj, a_class)
