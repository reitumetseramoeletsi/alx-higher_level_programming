#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for row in matrix:
        i = 0
        size = len(row) - 1
        for col in row:
            if i < size:
                print("{:d} ".format(col), end="")
                i = i + 1
            else:
                print("{:d}".format(col), end="")
        print()
