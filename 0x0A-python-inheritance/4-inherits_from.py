#!/usr/bin/python3
"""Module contains a function to print a given function """


def inherits_from(obj, a_class):
    """function to check if a object inherited from a given class only"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
