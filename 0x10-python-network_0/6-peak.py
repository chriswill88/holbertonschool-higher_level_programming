#!/usr/bin/python3


def find_peak(list_of_integers=[]):
    l = list_of_integers
    max = len(l)

    if max == 0:
        return None

    if l[0] > l[1]:
        return l[0]

    if l[-1] > l[-2]:
        return l[-1]

    i = 0
    while i + 2 < len(l):
        if l[i] <= l[i+1] >= l[i+2]:
            return l[i+1]
        i += 1
