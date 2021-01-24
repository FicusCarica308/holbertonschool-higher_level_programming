#!/usr/bin/python3
"""
Here we have a class called rectangle which inherits our base
class from our models.base module (this dicrectory)
"""
from models.base import Base


class Rectangle(Base):
    """
    In this class we intilize a new model from our superclass
    and setup a new rectangle class with attributes width, height, x, y,
    and id. ID is passed to the super class to initilize out model properly
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        inits our class with below arguments
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): X cordnate. Defaults to 0.
            y (int): Y cordnate. Defaults to 0.
            id (int): class Id of our model. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

# ---------------------WIDTH----------------
    @property
    def width(self):
        """
        a getter for the width private attribute
        Returns:
            [int]: value of width private attribute
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        a setter for the width private attribute
        Args:
            width (int): the new width value for the attribute
        """
        self.__width = width

# ---------------------HEIGHT----------------
    @property
    def height(self):
        """
        a getter for the height private attribute
        Returns:
            [int]: value of height private attribute
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        a setter for the height private attribute
        Args:
            height (int): the new height value for the attribute
        """
        self.__height = height

# ---------------------X-CORDNATE----------------
    @property
    def x(self):
        """
        a getter for the X private attribute
        Returns:
            [int]: value of X private attribute
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        a setter for the X private attribute
        Args:
            x (int): the new X value for the attribute
        """
        self.__x = x

# ---------------------Y-CORDNATE----------------
    @property
    def y(self):
        """
        a getter for the Y private attribute
        Returns:
            [int]: value of Y private attribute
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        a setter for the Y private attribute
        Args:
            y (int): the new Y value for the attribute
        """
        self.__y = y
