#!/usr/bin/python3
def max_integer(my_list=[]):
    high = 0
    if my_list is None:
        return None
    if len(my_list) == 0:
        return None
    for i in my_list:
        if i > high:
            high = i
    return high
