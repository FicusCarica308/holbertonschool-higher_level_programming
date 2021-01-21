#!/usr/bin/python3
"""Module that has a function that returns a value"""


def class_to_json(obj):
    """returns the dictionay representation of a object"""
    return obj.__dict__
