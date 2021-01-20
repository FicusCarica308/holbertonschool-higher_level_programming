#!/usr/bin/python3
"""Module contains a class the inherits BaseGerometry from file 7"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ defines a square using Rectangle """
    def __init__(self, size):
        """will init square with the init of rectangle"""
        super().integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def __str__(self):
        """returns a string of a square description"""
        return "[square] {0}/{0}".format(self.__size)
