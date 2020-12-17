#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_3 = list()
    for i in set_1:
        for x in set_2:
            if i == x:
                set_3.append(i)
    return set_3
