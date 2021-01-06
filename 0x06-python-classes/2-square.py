#!/usr/bin/python3
"""Class the creates a square"""


class Square:
    """Square class with a private field containing (__size)"""
    def __init__(self, size=0):
        """Function that initializes pivate attribute
        containing the size of the square with exception check
        to see if the given value is a integer or is positive
        """
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
