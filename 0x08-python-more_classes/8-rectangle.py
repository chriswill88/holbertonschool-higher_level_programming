#!/usr/bin/python3
""" Modual Rectangle """


class Rectangle:
    """ Rectangle Class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, (int)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, (int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if not self.__width or not self.__height:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        i = 0
        line = ""
        if not self.__width or not self.__height:
            return ""
        while i < self.__height:
            for x in range(self.__width):
                line += str(self.print_symbol)
            i += 1
            if i < self.height:
                line += "\n"
        return line

    def __repr__(self):
        return 'Rectangle(%s, %s)' % (self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area2 = rect_2.width * rect_2.height
        area1 = rect_1.width * rect_1.height
        if area1 == area2 or area1 > area2:
            return rect_1
        else:
            return rect_2
