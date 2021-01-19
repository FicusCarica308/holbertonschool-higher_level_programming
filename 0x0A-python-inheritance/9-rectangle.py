#!/usr/bin/python3
"""Module contains a class the inherits BaseGerometry from file 7"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that initilizes value using BaseGeomatry"""
    def __init__(self, width, height):
        """
        uses integer_validator from superclass to check given values
        and assigns them to private fields in rectangle class
        """
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self.__height = height
        self.__width = width

    def area(self):
        """returns the area of a square (overrides area in BaseGeometry"""
        return self.__width * self.__height

    def __str__(self):
        """returns a string of a rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
