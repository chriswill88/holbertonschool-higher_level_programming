#!/usr/bin/python3


def max_integer(my_list=[]):
    max, i = 0, 0
    if my_list is None:
        return None
    while i in range(len(my_list)):
        if (my_list[i] > max):
            max = my_list[i]
        i += 1
    return max
