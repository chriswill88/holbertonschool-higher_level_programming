#!/usr/bin/python3
"""islower checks if the passed in character is a lower case of uppercase"""


def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:  # Its checks if char is a lowercase
        return True
    return False
