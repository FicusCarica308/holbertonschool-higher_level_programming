#!/usr/bin/python3
""" Module that contains a function for writing files """


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        num_of_char = file.write(text)
    return num_of_char
