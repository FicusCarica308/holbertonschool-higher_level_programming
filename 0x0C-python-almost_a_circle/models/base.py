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
    def to_json_string(list_dictionaries=None):
        """ returns a JSON string from a dictionary """
        if type(list_dictionaries) is not list\
                and list_dictionaries is not None:
            raise TypeError("to_json_string: must be list of dict()")

        for dicti in list_dictionaries:
            if type(dicti) is not dict:
                raise ValueError("to_json_string: must be list of dict()")

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

# --------------JSON-TO-FILE---------------------
    @classmethod
    def save_to_file(cls, list_objs=None):
        """saves json string repr of a list of object-dicts repr to a file"""

        list_dict = []

        if list_objs is not None:
            if type(list_objs) is not list:
                raise TypeError("save_to_file: arg must be list() of objs")
            for obj in list_objs:
                if obj is None or isinstance(obj, Base) is not True:
                    raise ValueError("save_to_file: obj's in list must be "
                                     "instances of Square or Rectangle")
                list_dict.append(obj.to_dictionary())
            string_rep = cls.to_json_string(list_dict)
        else:
            string_rep = "[]"
        with open("{}.json".format(cls.__name__),
                  mode="w", encoding="utf-8") as file:
            file.write(string_rep)
