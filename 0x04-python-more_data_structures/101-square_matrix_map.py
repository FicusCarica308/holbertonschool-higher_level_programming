#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda idx: list(map(lambda x: x*x, idx)), matrix))