#!/usr/bin/python3
from calculator_1 import add, sub, div, mul
from sys import argv


if __name__ == "__main__":  # no run from import
    if len(argv) != 4:  # fail case 1: not right amount of arguments
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])  # first number
    b = int(argv[3])  # second number

    """ this part is for finding the operatior and getting the results """
    if argv[2] == '+':
        res = add(a, b)
    elif argv[2] == '-':
        res = sub(a, b)
    elif argv[2] == '*':
        res = mul(a, b)
    elif argv[2] == '/':
        res = div(a, b)

    else:  # fail case unknow operator
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(argv[1], argv[2], argv[3], res))  # prints out
