#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
modual inherits BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    class Rectangle

    Attributes:
        width: the width of the rectangle
        height: height of the rectangle

    Methods:
        integer_validator - inherited value checker
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        print(self.__width)

        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
