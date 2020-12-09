#!/usr/bin/python3
def remove_char_at(str, n):
    if n > -1:
        str_cpy = str[0:n] + str[n + 1:]
        return str_cpy
    else:
        return str
