#!/usr/bin/python3
"""Module that has a function using json encoding"""


def class_to_json(obj):
    """converts a class to json"""
    return obj.__dict__
