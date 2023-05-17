#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(map(lambda vertex: list(map(lambda number: number ** 2, vertex)), matrix))
    return new_matrix
