#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    i = 0
    tuppy = []
    while i < 2:
        try:
            a = int(tuple_a[i])
        except IndexError:
            a = 0
        try:
            b = int(tuple_b[i])
        except IndexError:
            b = 0
        tuppy.append(b + a)
        i += 1
    return tuple(tuppy)
