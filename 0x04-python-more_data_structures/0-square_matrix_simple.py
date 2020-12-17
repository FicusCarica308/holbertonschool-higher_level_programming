#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for row1 in new_matrix:
        for idx in range(0, len(row1)):
            row1[idx] = row1[idx]**2
    return new_matrix
