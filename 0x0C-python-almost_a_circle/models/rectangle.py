#!/usr/bin/python3
from models.base import Base
"""
model.base contains Rectangle class
"""


class Rectangle(Base):
    """
    Class Rectangle - creates rectangle object
    inherits from the Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Method Name __init__
        Purpose: Class Constructor
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        self.__id = super().__init__(id)

    @property
    def width(self):
        """ Getter for Width """
        return self.__width

    @width.setter
    def width(self, width=0):
        """ Setter for width """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, height=0):
        """ Setter for height """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, x=0):
        """ Setter for x """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, y=0):
        """ Setter for y """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
            self.__y = y

    def area(self):
        """
        Method Name: area
        Purpose: returns area
        """
        return self.__width * self.__height

    def display(self):
        """
        Method Name: display
        Purpose: to display rectangles
        """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        Method Name: __str__
        Purpose: prints params
        """
        s = self
        i = s.id
        x = s.__x
        y = s.__y
        w = s.__width
        h = s.__height
        srt = '[{}] ({}) {}/{} - {}/{}'.format(type(s).__name__, i, x, y, w, h)
        return srt

    def update(self, *args, **kwargs):
        """
        Method Name: update
        Purpose: using *args and **kwargs update attributes
        """
        i = 0
        if len(args) == 0 and not args:
            for k, v in kwargs.items():
                if k is "id":
                    self.id = v
                if k == "width":
                    self.__width = v
                if k == "height":
                    self.__height = v
                if k == "x":
                    self.__x = v
                if k == "y":
                    self.__y = v
        else:
            for a in args:
                if i == 0:
                    self.id = a
                if i == 1:
                    self.__width = a
                if i == 2:
                    self.__height = a
                if i == 3:
                    self.__x = a
                if i == 4:
                    self.__y = a
                i += 1

    def to_dictionary(self):
        s = self
        h = "height"
        w = "width"
        i = 'id'
        return {'x': s.__x, 'y': s.__y, i: s.id, h: s.__height, w: s.__width}

