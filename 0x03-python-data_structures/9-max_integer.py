#!/usr/bin/python3


def max_integer(my_list=[]):
    max = 0
    i = 0

    if my_list is None or my_list is []:
        return None
    while i in range(len(my_list)):
        print(my_list[i])
        if (my_list[i] > max):
            max = my_list[i]
        i += 1
    return max
