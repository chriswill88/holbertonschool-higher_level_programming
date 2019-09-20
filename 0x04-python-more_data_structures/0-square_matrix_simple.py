#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    m = matrix
    lis = [[m[x][y] ** 2 for y in range(len(m[x]))] for x in range(len(m))]
    return lis
