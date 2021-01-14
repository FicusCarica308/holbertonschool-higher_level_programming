#!/usr/bin/python3
"""
2-add_integer.py:
    This Module contains a function method that will divide a
    given matrix of integers/floats by a given divisor
"""


def matrix_divided(matrix=None, div=None):
    """
    matrix_divided:
        divides a matrix of float/int by a given divisor
    Paramaters:
    matrix(list)needs to be integers: matrix of integers input
    div(int): our divisors

    Returns:
        returns a new matrrx with the result of each division
        rounded to the second decimal place
    """
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    if isinstance(matrix, list) is not True or matrix[0] is None:
        raise TypeError(matrix_error)
    for x in matrix:
        if type(x) is not list:
            raise TypeError(matrix_error)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif isinstance(div, (int, float)) is not True:
        raise TypeError("div must be a number")

    new_matrix = [row[:] for row in matrix]
    row_lgt = len(matrix[0])

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if isinstance(matrix[row][column], (int, float)) is not True:
                raise TypeError(matrix_error)
            new_matrix[row][column] = round(matrix[row][column] / div, 2)
        if column != row_lgt - 1:
            raise TypeError("Each row of the matrix must have the same size")

    return new_matrix
