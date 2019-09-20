#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    lis = [[matrix[x][y] ** 2 for y in range(3)] for x in range(3)]
    return lis
