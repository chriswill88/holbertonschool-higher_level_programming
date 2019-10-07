#!/usr/bin/python3
""" Doc this modual is for defining a
function that divides a matrix by a number
returning a new matrix with solutions
"""


def matrix_divided(matrix, div):
    """
    matrix_divided - divides a matrix by a number

    list1 - the returned list
    number - makes sure we have the first index of a inside list
    index1 - gives use the index of an embeded list

    Return: list1 - matrix of divided solutions
    """
    list1 = []
    number = 0
    index1 = 0

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        number = 0
        try:
            for x in i:
                if number == 0:
                    list1.append([])
                if not isinstance(x, (int, float)):
                    raise TypeError("matrix must be a \
                                    matrix (list of lists) of integers/floats")
                list1[index1].append(round((x / div), 2))
                number += 1
        except:
            raise TypeError("matrix must be a \
                matrix (list of lists) of integers/floats")
        if len(matrix[index1]) != len(list1[index1]):
            raise TypeError("Each row of the matrix must have the same size")
        index1 += 1
    return list1
