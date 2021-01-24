#!/usr/bin/python3
"""This module contains a class with two definitions"""


class Student:
    """
    A class that defines a student object with a first name, last name
    and an age...
    """
    def __init__(self, first_name, last_name, age):
        """creates three public instance attributes (first, last, age)"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary representation of the current object"""
        if attrs is None:
            return self.__dict__
        new_dict = dict()
        for atr in attrs:
            for key in self.__dict__:
                if atr == key:
                    new_dict[key] = self.__dict__[key]
        return new_dict

    def reload_from_json(self, json):
        """ will remove and add new attributes and values given in json """
        for key_rm in dict(self.__dict__):
            try:
                setattr(self, key_rm, json[key_rm])
            except:
                pass
