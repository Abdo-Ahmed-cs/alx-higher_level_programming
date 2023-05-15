#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print()
    else:
        for vertex in matrix:
            for item in vertex:
                print("{:d}".format(item), end=" ")
            print()
