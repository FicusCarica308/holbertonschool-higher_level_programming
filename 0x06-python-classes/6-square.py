#!/usr/bin/python3
"""Class the creates a square"""


class Square:
    """Square class with a private field containing (__size)

    SETTER/GETTER
    >>contains a getter and setter property for our private attribute size
    (setter is called during __init__) Property:(size)
    -------------------------------------------
    >>contains a getter and setter property for our private attribute positon
    (setter is called during __init__) Property:(positIon)

    DEFS:
    >>Contains a definition that prints out the square
    using # in stdout name:(my_print)
    --------------------------------------------
    >>Cointains def that returns the area of the square name:(area)
    """
    def __init__(self, size=0, position=(0, 0)):
        """initilizes our private field attributes __size &
        __position by calling their setter on self
        """
        self.size = size
        self.position = position

    def area(self):
        """function to return the area of the square class"""
        return self.__size * self.__size

    @property
    def position(self):
        """getter definintion that returns the value of
        private attribute position (my_square.position) to call
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Function that initializes pivate attribute
        containing the position of the square with exception check
        to see if the given value is a tuple or is positive
        USAGE: class_name.position = new_value
        """
        if isinstance(value, tuple) is not True\
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @property
    def size(self):
        """getter definintion that returns the value of
        private attribute size (my_square.size) to call
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

    def my_print(self):
        """prints out our square using size in stdout with #
        while also leaving spaces in the front of each line based on the
        position of the square given as tuple (only position[0] is used)
        """
        for k in range(self.position[1]):
                print("")
        for i in range(0, self.size):
            for j in range(0, self.size + self.position[0]):
                if j < self.position[0]:
                    print(" ", end="")
                else:
                    print("#", end="")
            print()
        if self.size == 0:
            print()
