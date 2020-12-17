#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    num = 0
    num_hold = 0
    key_hold = ""
    for key in a_dictionary:
        num = a_dictionary.get(key, None)
        if num == None:
            num = 0
        if num > num_hold:
            key_hold = key
        num_hold = a_dictionary.get(key_hold, None)
    return key_hold
