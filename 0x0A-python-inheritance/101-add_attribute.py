#!/usr/bin/python3
"""holds a function that adds a attribute to a given object"""


def add_attribute(obj, name, value):
    """
    This function will add a attribute to a given object
    on failure will raise TypeError with message
    """
    for i in dir(obj):
        if i == "__dict__":
            obj.name = lambda: None
            setattr(obj, name, value)
            return
    raise TypeError("can't add new attribute")
