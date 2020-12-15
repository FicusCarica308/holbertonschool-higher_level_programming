#!/usr/bin/python3
def max_integer(my_list=[]):
    high = 0
    for i in my_list:
        if i > high:
            high = i
    return high
