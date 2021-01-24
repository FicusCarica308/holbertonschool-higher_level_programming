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

    def to_json(self):
        """returns the dictionary representation of the current object"""
        return self.__dict__
