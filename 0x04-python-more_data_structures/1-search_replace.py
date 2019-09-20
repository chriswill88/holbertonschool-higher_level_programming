#!/usr/bin/python3


def search_replace(my_list, search, replace):
    lis = []
    for i in range(len(my_list)):
        if my_list[i] is search:
            lis.append(replace)
        else:
            lis.append(my_list[i])
    return lis
