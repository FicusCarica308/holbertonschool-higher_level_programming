#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tuple_none = (0, None)
        return tuple_none
    tuple_full = (len(sentence), sentence[0])
    return tuple_full
