#!/usr/bin/python3
"""
Contains a new class that inherits from Rectangle in
models module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square creates a instance using Rectangle to initiate it
    with the width and height being the same
    Args:
        Rectangle (class): creates a instance of a rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initiates our square instance
        Args:
            size (int): the size of our square (width, height)
            x (int): x cordnate. Defaults to 0.
            y (int): y cordnate . Defaults to 0.
            id ([Type]): number id of instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

# --------------------------SIZE-------------------------------
    @property
    def size(self):
        """
        Returns:
            int: returns the width or "size" of our "square"
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        sets our square to a new size by changing width and height
        Args:
            size (int): the new size for our square instance
        """
        self.width = size
        self.height = size

# -----------------------STR--------------------------
    def __str__(self):
        """ returns a printable string rep of our square """
        string = "[Square] ({}) {}/{} - {}"
        return string.format(self.id, self.x, self.y, self.width)

# ----------------------UPDATE-------------------------
    def update(self, *args, **kwargs):
        """
        updates attributes for square based on args and kwargs
        """
        attrs = ["id", "size", "x", "y"]
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
            return

        for index in range(len(args)):
            setattr(self, attrs[index], args[index])
