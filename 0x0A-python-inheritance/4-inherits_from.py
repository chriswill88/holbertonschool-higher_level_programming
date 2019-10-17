#!/usr/bin/python3
"""
This modual contains the program inherits from
"""


def inherits_from(obj, a_class):
    """
    inherits_from - checks if obj is of a_class

    Parameters:
        obj - the object
        a_class - the class

    Returns:
        True if obj inherits from a_class
        or False if not
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
