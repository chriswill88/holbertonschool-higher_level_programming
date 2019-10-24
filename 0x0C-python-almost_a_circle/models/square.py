#!/usr/bin/python3
"""Square contains Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square: creates a square object
    """
    def __init__(self, size, x=0, y=0, id=None):
        """class Constructor"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(Rectangle):
        """
        Method Name: __str__
        purpose: prints - attributes
        """
        s = Rectangle
        i = s.id
        # print("i =", i)
        x = s.x
        y = s.y
        w = s.width
        srt = '[{}] ({}) {}/{} - {}'.format(type(s).__name__, i, x, y, w)
        return srt

    @property
    def size(self):
        """ getter for size"""
        return self.width

    @size.setter
    def size(self, vari):
        """ Setter for size """
        if not isinstance(self.width, int):
            raise TypeError("size must be an integer")
        if self.width <= 0:
            raise ValueError("size must be > 0")
        self.width = vari
        self.height = vari

    def update(self, *args, **kwargs):
        """ update: updates attributes using args and kwargs"""
        i = 0
        s = self
        if len(args) == 0 and not args:
            i = 0
            for k, v in kwargs.items():
                # print("square: key->", k, "val->", v)
                if k == "id":
                    s.id = v
                    # print("sq - kwargs - id = ", s.id)
                if k == "size" or k == "width":
                    s.width = v
                if k == "x":
                    s.x = v
                if k == "y":
                    # print("y found")
                    Rectangle.y = v
                    # print("y =", Rectangle.y)
        else:
            i = 0
            for a in args:
                # print("val->", a)
                if i == 0:
                    s.id = a
                # print("sq - args - id = ", s.id)
                if i == 1:
                    s.width = a
                if i == 2:
                    s.x = a
                if i == 3:
                    s.y = a
                i += 1
        # print("------------------")

    def to_dictionary(self):
        """ return a dictionary reperesentation of object """
        s = self
        return {'id': s.id, 'x': s.x, 'size': s.width, 'y': s.y}
