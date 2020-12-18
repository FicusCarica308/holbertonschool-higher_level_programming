#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy = dict(a_dictionary)
    for key in copy:
        if copy[key] == value:
            a_dictionary.pop(key, None)
    return a_dictionary
