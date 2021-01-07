#!/usr/bin/python3
import math
"""This is decoded from ByteCode"""


class MagicClass:
    """MAGIC CLASS"""
    def __init__(self, radius):
        """doc string 1"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self, radius):
        """doc string 2"""
        return self.__radius ** 2 * math.pi

    def circumference(self, radius):
        """doc string 3"""
        return 2 * math.pi * self.__radius
