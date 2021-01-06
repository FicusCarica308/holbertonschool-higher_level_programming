#!/usr/bin/python3
"""Class the creates a square"""


class Square:
    """Square class with a private field containing (__size)
    and a definitions that returns the area of the square.

    Also contains a getter and setter property for our private attribute size
    (setter is called during __init__)
    """
    def __init__(self, size=0):
        """initilizes our private field attribute __size
        by calling its setter
        """
        self.size = size

    def area(self):
        """function to return the area of the square class"""
        return self.__size * self.__size

    @property
    def size(self):
        """getter definintion that returns the value of
        private attribute size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Function that initializes pivate attribute
        containing the size of the square with exception check
        to see if the given value is a integer or is positive
        USAGE: class_name.size = new_value
        """
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
        
        # --------------------------------------------
    def __eq__(self, other):
        return (self.__size * self.__size) == (other.__size * other.__size)
    def __lt__(self, other):
        return (self.__size * self.__size) < (other.__size * other.__size)
    def __le__(self, other):
        return (self.__size * self.__size) < (other.__size * other.__size)
    def __ne__(self, other):
        return (self.__size * self.__size) < (other.__size * other.__size)
    def __gt__(self, other):
        return (self.__size * self.__size) < (other.__size * other.__size)
    def __ge__(self, other):
        return (self.__size * self.__size) < (other.__size * other.__size)
