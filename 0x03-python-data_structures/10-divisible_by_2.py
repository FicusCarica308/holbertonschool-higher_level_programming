#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list = [True] * len(my_list)
    cnt = 0
    for i in my_list:
        if i % 2 == 0:
            list[cnt] = True
        else:
            list[cnt] = False
        cnt = cnt + 1
    return list
