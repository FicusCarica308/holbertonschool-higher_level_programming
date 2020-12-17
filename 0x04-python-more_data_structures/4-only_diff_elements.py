#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = list()
    for i in set_1:
        if i not in set_2:
            set_3.append(i)
    for k in set_2:
        if k not in set_1:
            set_3.append(k)
    return set_3
