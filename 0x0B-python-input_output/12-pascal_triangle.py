#!/usr/bin/python3
"""Module that contains a function that prints a pascal triangle"""


def pascal_triangle(n):
    """prints a pasal trianlge using the powers of 11 !!!!"""
    row = []
    matrix = []
    current = 0
    if n <= 0:
        return []
    for i in range(0, n):
        row = []
        current = 11**i
        for i in str(current):
            row.append(int(i))
        matrix.append(row)
    return matrix
