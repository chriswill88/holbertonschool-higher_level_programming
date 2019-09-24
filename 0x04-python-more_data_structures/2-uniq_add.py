#!/usr/bin/python3


def uniq_add(my_list=[]):
    sum = 0
    lis = []
    for i in my_list:
        if i not in lis:
            lis.append(i)
    for i in lis:
        sum += i

    return sum
