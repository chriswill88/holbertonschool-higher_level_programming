#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    lis = [[matrix[x][y] ** 2 for y in range(len(matrix[x]))] for x in range(len(matrix))]
    return lis
