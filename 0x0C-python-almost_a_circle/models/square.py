#!/usr/bin/python3
from models.rectangle import Rectangle
"""
models.square contains Square class
"""


class Square(Rectangle):
    """
    class Square: creates a square object
    """
    def __init__(self, size, x=0, y=0, id=None):
        """class Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(Rectangle):
        """
        Method Name: __str__
        purpose: prints - attributes
        """
        s = Rectangle
        i = Rectangle.id
        x = s.x
        y = s.y
        w = s.width
        srt = '[{}] ({}) {}/{} - {}'.format(type(s).__name__, i, x, y, w)
        return srt

    @property
    def size(self, size=0):
        return size

    @size.setter
    def size(self, size=0):
        """ Setter for size """
        if not isinstance(self.width, int):
            raise TypeError("size must be an integer")
        if self.width <= 0:
            raise ValueError("size must be > 0")
        self.width = size
        if not isinstance(self.height, int):
            raise TypeError("height must be an integer")
        if self.height <= 0:
            raise ValueError("height must be > 0")
        self.height = size
