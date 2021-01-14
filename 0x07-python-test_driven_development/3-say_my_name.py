#!/usr/bin/python3
"""
3-say_my_name.py:
    This Module contains a function method that prints
    out a given name (first, last)
"""


def say_my_name(first_name=None, last_name=None):
    """
    say_my_name:
        prints first_name and last_name in stdout
    Paramaters:
        first_name(string) = first name of user
        last_name(string) = last name of user
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
