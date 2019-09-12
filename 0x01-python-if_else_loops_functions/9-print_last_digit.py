#!/usr/bin/python3


def print_last_digit(number):
    """prints and returns the last digit"""
    a = str(number)[len(str(number)) - 1]  # converts an int into a string
    print("{}".format(a), end="")  # prints the last digit
    return int(a)  # returns the last digit
