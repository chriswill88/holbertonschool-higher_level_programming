#!/usr/bin/python3


class Square:
    """
    Creating a Class: Square
    Attributes|
        Private Instance Variable: __size
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """
        Public instance method: area
        returns the area based on the size
    """
    def area(self):
        size = self.__size
        return size * size

    def my_print(self):
        size = self.size
        position = self.__position
        for x in range(position[1]):
            print()
        for i in range(size):
            print(" " * position[0], end='')
            print('#' * size)
        if size == 0:
            print()
