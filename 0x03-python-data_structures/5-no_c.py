#!/usr/bin/python3
def no_c(my_string):
    x = 0
    copy = my_string
    for i in copy:
        if i == 'c' or i == 'C':
            copy = copy[:x] + copy[x + 1:]
            x -= 1
        x = x + 1
    my_string = copy
    return my_string
