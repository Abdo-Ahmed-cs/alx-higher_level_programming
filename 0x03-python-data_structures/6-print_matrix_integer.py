#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print()
    else:
        for vertex in matrix:
            for index in range(len(vertex)):
                if index < len(vertex) - 1:
                    print("{:d}".format(vertex[index]), end=" ")
                else:
                    print("{:d}".format(vertex[index]), end="")
            print()
