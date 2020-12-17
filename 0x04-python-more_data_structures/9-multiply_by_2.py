#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy = a_dictionary.copy()
    for key in copy:
        copy[key] = copy.get(key, None) * 2
    return copy
