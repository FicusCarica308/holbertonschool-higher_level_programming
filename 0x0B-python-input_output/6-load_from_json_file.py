#!/usr/bin/python3
""" module that contains a function using json encoding """
import json


def load_from_json_file(filename):
    """
    writes an python Object to a text file, using a JSON representation
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        obj = json.load(file)
    return obj
