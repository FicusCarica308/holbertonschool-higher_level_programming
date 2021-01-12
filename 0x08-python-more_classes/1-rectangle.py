#!/usr/bin/python3
"""Class that creates a Rectangle object"""


class Rectangle:
    """Empty Class"""
    def __init__(self, width=0, height=0):
        """Private field initilizer"""
        self.width = width
        self.height = height
# ============================================================

    @property
    def width(self):
        """getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
# ============================================================

    @property
    def height(self):
        """getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height private attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
# ============================================================
