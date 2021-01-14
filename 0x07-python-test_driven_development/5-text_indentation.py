#!/usr/bin/python3
"""module contains a def to add new lines to a given text"""


def text_indentation(text=None):
    """The def that adds the new lines"""
    new_string = ""
    print_string = ""
    found = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        new_string += text[i]
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            found += 1
            new_string += "\n\n"
    for i in range(len(new_string)):
        if new_string[i] == ' ' and new_string[i - 1] == '\n':
            continue
        print_string += new_string[i]
    if found > 0:
        print(print_string, end="")
    else:
        print(print_string)
