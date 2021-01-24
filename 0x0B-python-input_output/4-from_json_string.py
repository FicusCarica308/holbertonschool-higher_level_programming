#!/usr/bin/python3
""" module that contains a function using json encoding """
import json


def from_json_string(my_str):
    """ returns the python representation of a JSON string """
    return json.loads(my_str)
