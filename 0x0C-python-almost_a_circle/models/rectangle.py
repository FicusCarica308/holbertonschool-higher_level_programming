#!/usr/bin/python3
"""
Here we have a class called rectangle which inherits our base
class from our models.base module (this dicrectory)
"""
from models.base import Base


def raise_exc(attribute="", error=""):
    """
    raises an exception based on attribute and error information
    Args:
        attribute (str): what attr we are rasing for. Defaults to "".
        error (str): what error we are rasing. Defaults to "".
        - Error should be one of two type "Type" or "Raise"

    Raises:
        TypeError: Raises if "Type" is True for any attr
        ValueError(one): (raises if x or y)
        ValueError(two): raises for width or height
    """
    if error == "Type":
        raise TypeError("{} must be an integer".format(attribute))
    elif error == "Value":
        if attribute == "x" or attribute == "y":
            raise ValueError("{} must be >= 0".format(attribute))
        else:
            raise ValueError("{} must be > 0".format(attribute))


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
        if type(width) is not int:
            raise_exc("width", "Type")
        elif width <= 0:
            raise_exc("width", "Value")
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
        if type(height) is not int:
            raise_exc("height", "Type")
        elif height <= 0:
            raise_exc("height", "Value")
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
        if type(x) is not int:
            raise_exc("x", "Type")
        elif x < 0:
            raise_exc("x", "Value")
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
        if type(y) is not int:
            raise_exc("y", "Type")
        elif y < 0:
            raise_exc("y", "Value")
        self.__y = y
