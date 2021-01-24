#!/usr/bin/python3
""" module containg a function to append to a file """


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file
    (UTF8) and returns the number of chars
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        num_of_char = file.write(text)
    return num_of_char
