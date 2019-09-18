#!/usr/bin/python3


def max_integer(my_list=[]):
    i = 0
    if len(my_list) == 0:
        return None
    max = my_list[i]
    if len(my_list) == 0:
        return None
    while i in range(len(my_list)):
        if (my_list[i] > max):
            max = my_list[i]
        i += 1
    return max
