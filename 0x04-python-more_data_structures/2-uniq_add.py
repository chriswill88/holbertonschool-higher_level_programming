#!/usr/bin/python3


def uniq_add(my_list=[]):
    sum = 0
    x = 0
    for i in range(len(my_list)):
        check = my_list[i]
        x == 0
        while x < i - 1:
            if x < i and my_list[i] == check:
                sum += check
                break
            x += 1

    return sum
