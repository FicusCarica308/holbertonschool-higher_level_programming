#!/usr/bin/python3
""" contains one function to test if objects are the same"""


def is_same_class(obj, a_class):
    """ Tests if object given object is the same"""
    if obj.__class__ != a_class:
        return False
    return True
