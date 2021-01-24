#!/usr/bin/python3
"""
This file contains our base class for our models project.
"""
import json


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

# ---------------DICT-TO-JSON-STR--------------
    def to_json_string(list_dictionaries):
        """ returns a JSON string from a dictionary """
        if list_dictionaries is None or list_dictionaries[0] is None:
            return "[]"
        return json.dumps(list_dictionaries)
