#!/usr/bin/python3
""" This module contains a function to print out a file """


def read_file(filename=""):
    """ reads a text file(filename) in (UTF8) and prints it to stdout """
    with open(filename, mode='r', encoding='utf-8') as file:
        for a_line in file:
            print(a_line, end="")
