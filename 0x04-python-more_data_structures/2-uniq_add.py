#!/usr/bin/python3
def uniq_add(my_list=[]):
    copy = my_list[:]
    cnt = 0
    sum = 0
    for i in range(0, len(my_list)):
        for x in range(0, len(my_list)):
            if my_list[i] == my_list[x]:
                cnt = cnt + 1
        if cnt > 1:
            copy[i] = 0
        cnt = 0
    print(copy)
    for k in copy:
        if k != 0:
            sum = sum + k
    return sum
