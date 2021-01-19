#!/usr/bin/python3
""" contains one function to test if objects are from a certain class"""


def is_kind_of_class(obj, a_class):
    """
    Tests if object given is the same
    class or subclass of the given class
    """
    return isinstance(obj, a_class)
