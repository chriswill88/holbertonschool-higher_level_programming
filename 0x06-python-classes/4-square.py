#!/usr/bin/python3


class Square:
    """
    Creating a Class: Square
    Attributes|
        Private Instance Variable: __size
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if 0 > value:
            raise ValueError("size must be >= 0")
        self.__size = value
    """
        Public instance method: area
        returns the area based on the size
    """
    def area(self):
        size = self.__size
        return size * size
