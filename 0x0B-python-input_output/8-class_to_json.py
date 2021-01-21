#!/usr/bin/python3
"""Module that has a function using json encoding"""
import json


def class_to_json(obj):
    """converts a class to json"""
    other = json.dumps(obj.__dict__)
    return json.loads(other)
