#!/usr/bin/python3
"""Class the creates a square"""


class Square:
    """Square class with a size private field (__size)"""
    def __init__(self, size=0):
        """Function that initializes pivate attribute
        containing the size of the square
        """
        self.__size = size
