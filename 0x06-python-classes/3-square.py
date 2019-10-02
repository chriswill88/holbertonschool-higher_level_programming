#!/usr/bin/python3


class Square:
    """
    Creating a Class: Square
    Attributes|
        Private Instance Variable: __size
    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if 0 > self.__size:
            raise ValueError("size must be >= 0")
    """
        Public instance method: area
        returns the area based on the size
    """
    def area(self):
        size = self.__size
        return size * size
