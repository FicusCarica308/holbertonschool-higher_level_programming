#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_acpy = ()
    tuple_bcpy = ()
    if len(tuple_a) == 0:
        tuple_acpy = (0, 0)
    elif len(tuple_a) == 1:
        tuple_acpy = (tuple_a[0], 0)
    else:
        tuple_acpy = tuple_a
    if len(tuple_b) == 0:
        tuple_bcpy = (0, 0)
    elif len(tuple_b) == 1:
        tuple_bcpy = (tuple_b[0], 0)
    else:
        tuple_bcpy = tuple_b
    first = tuple_acpy[0] + tuple_bcpy[0]
    second = tuple_acpy[1] + tuple_bcpy[1]
    tuple_c = (first, second)
    return tuple_c
