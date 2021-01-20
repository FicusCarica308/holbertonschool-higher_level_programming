#!/usr/bin/python3
"""Module with a single class"""


class BaseGeometry:
    """empy class"""

    def area(self):
        """raises a excpetion from BaseException"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """tests if given value is a integer and greater than 0"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
