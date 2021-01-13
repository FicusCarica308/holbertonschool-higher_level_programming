#!/usr/bin/python3
"""
0-add_integer.py:
    This Module contains a function method that adds two
    given integers together.
"""


def add_integer(a, b=98):
    """
    add_integer:
        adds two integers/floats
    Paramaters:
    a (int or float): intger input by user
    b (int or float): integer input by user

    Returns:
        returns the addition of parameters a and b (a + b)

    Examples:
        Integers:
        >>> add_integer(2, 2)
        4

        Floats: (rounds down since floats are casted to ints)
        >>> add_integer(5.7, 5.4)
        10
    """
    if isinstance(a, (int, float)) is not True:
        raise TypeError("a must be an integer")
    elif isinstance(b, (int, float)) is not True:
        raise TypeError("b must be an integer")
    try:
    a = int(a)
    b = int(b)
    except OverflowError:
        return
    return a + b
