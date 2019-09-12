#!/usr/bin/python3


def uppercase(str):
    i = 0
    while i < len(str):
        if ord(str[i]) in range(97, 122):
            a = chr((ord(str[i]) - ord('a')) + ord('A'))
        else:
            a = str[i]
        print("{}".format(a), end="")
        i += 1
    print()
