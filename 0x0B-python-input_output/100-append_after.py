#!/usr/bin/python3
"""module contains a function that adds a new line to a file"""


def append_after(filename="", search_string="", new_string=""):
    """function that locates a given line and prints a custome line after"""
    line_index = []
    count = 0
    added = 0
    with open(filename, mode="r", encoding="utf-8") as file:
        lines = file.readlines()
    for index in lines:
        count += 1
        if search_string in index:
            line_index.append(count)
    for i in line_index:
        lines.insert(int(i) + added, new_string)
        added += 1
    with open(filename, mode="w", encoding="utf-8") as file:
        pass
    for j in lines:
        with open(filename, mode="a", encoding="utf-8") as file:
            file.write(j)
