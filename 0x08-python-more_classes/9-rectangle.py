#!/usr/bin/python3
"""This is a example class"""


class Rectangle:
    """A rectangle class with width and height"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This initializes the width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method for area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """method for perimiter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """returns rectangle as string"""
        square_str = ""
        if self.__width == 0 or self.__height == 0:
            square_str = "\n"
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    square_str += str(self.print_symbol)
                square_str += "\n"
        return square_str[:-1]

    def __repr__(self):
        """returns string as code"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """runs when object is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """returns bigger rectangle"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """returns new Rectangle with same width, height"""
        return cls(size, size)
