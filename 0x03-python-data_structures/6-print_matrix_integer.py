#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for inner in matrix:
        for i in range(0, len(inner)):
            print("{}".format(inner[i]), end="")
            if i < len(inner) - 1:
                print(" ", end="")
        print()