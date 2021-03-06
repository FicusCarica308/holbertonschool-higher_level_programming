#!/usr/bin/python3
"""Class that creates a Rectangle object"""


class Rectangle:
    """Empty Class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Private field initilizer"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
# ============================================================

    @property
    def width(self):
        """getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width attribute"""
        if type(value) is not int:
            raise TypeError("width must be and integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
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

    def area(self):
        """gets the area of the rectangle object"""
        return self.height * self.width

    def perimeter(self):
        """gets the perimeter of the rectangle object"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * self.width) + (2 * self.height)
# ============================================================

    def __str__(self):
        """when print() is called prints square using '#'"""
        output = ""
        if self.height == 0 or self.width == 0:
            return output
        else:
            for height in range(self.height):
                for width in range(self.width):
                    output += str(self.print_symbol)
                if height != self.height - 1:
                    output += '\n'
        return output

    def __repr__(self):
        """returns data for program to recreate a class object"""
        return "Rectangle({self.width}, {self.height})".format(self=self)
# ============================================================

    def __del__(self):
        """prints message on object deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
# ============================================================
