#!/usr/bin/python3
"""
This file contains our base class for our models project.
"""


class Base:
    """
    This is our base class that will be inherited by every other class
    in this project.

    Private class attribute:
        __nb_objects(int) - keeps track of the number
            of objects currently being used
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Args:
            id (int): The id of the called class. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
