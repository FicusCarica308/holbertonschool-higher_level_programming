#!/usr/bin/python3
def islower(c):
    value = ord(c)
    for i in range(65, 91):
        if value == i:
            return False
    for j in range(97, 123):
        if value == j:
            return True
    return False
