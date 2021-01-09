#!/usr/bin/python3
"""prints a square"""


def print_square(size):
    """prints out our square using size in stdout with #"""
    if isinstance(size, int) is not True:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
    if size == 0:
        print()
