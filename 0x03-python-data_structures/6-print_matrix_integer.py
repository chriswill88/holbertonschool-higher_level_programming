#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """ prints a matrix"""
    i = 0
    x = 0
    while i in range(len(matrix)):  # looping through columns
        while x in range(0, len(matrix[i])):  # looping through rows
            str = "{:d}"
            print(str.format(matrix[i][x]), end="")
            if x < len(matrix[i]) - 1:  # printing spaces
                print(" ", end="")
            x += 1
        print()  # printing newline
        x = 0
        i += 1
