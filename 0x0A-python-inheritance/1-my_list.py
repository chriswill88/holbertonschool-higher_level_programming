#!/usr/bin/python3
"""
This modual contains the class MyList
"""


class MyList(list):
    """
    MyList - A Class

    Inherits from the list class

    Methods:
        print_sorted - prints a sorted list
    """
    def print_sorted(self):
        """
        print_sorted - prints a sorted list
        """
        print(sorted(self))
