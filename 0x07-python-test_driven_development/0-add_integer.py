#!/usr/bin/python3
"""
This modual is for adding two numbers
"""


def add_integer(a, b=98):
    """
    add_integers - adds two numbers

    a - a number
    b - a number

    Return: the sum
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    results = int(a + b)
    return results
