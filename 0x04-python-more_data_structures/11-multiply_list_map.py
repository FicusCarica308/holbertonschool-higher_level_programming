#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    copy = my_list.copy()
    copy[:] = map(lambda x: x*number, copy)
    return copy
