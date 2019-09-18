#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    i = 0
    new_list = []
    while i in range(len(my_list)):
        if int(my_list[i]) % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
        i += 1
    return new_list
