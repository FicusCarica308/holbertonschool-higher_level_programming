#!/usr/bin/python3
"""File that contains a main to add a item to a new file"""
import sys
load_from = __import__('6-load_from_json_file').load_from_json_file
save_to = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"
try:
    obj = load_from(filename)
except FileNotFoundError:
    with open(filename, mode='w', encoding="utf-8"):
        obj = list()
obj += sys.argv[1:]
save_to(obj, filename)
