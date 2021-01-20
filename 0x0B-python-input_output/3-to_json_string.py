#!/usr/bin/python3
""" module that contains a function using json encoding """
import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string)
    in other words converts a python object to a json string
    """
    return json.dumps(my_obj)
