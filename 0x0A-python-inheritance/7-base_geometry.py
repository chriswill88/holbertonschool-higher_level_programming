#!/usr/bin/python3
"""
This modual contains the class BaseGeometry
"""


class BaseGeometry:
    """
    Class BaseGeometry

    Methods:
        area()
    """
    def area(self):
        """
        area - empty method in BaseGeometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator - checks that value meets cetain requirements
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
