#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    grades = list()
    weights = list()
    sum = 0
    div = 0
    for i in range(0, len(my_list)):
        for j in [0]:
            grades.append(my_list[i][j])
        for j in [1]:
            weights.append(my_list[i][j])
    for i in range(0, len(my_list)):
        sum = sum + (weights[i] * grades[i])
        div = div + weights[i]
    return sum / div
