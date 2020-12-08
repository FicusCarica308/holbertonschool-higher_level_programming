#!/usr/bin/python3
def uppercase(str):
    value = 0
    for i in str:
        value = ord(i)
        if value > 96 and value < 123:
            value = value - 32
        print("{}".format(chr(value)), end="")
    print()
