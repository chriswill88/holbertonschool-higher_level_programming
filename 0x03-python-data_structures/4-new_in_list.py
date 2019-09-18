#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """ creates a node and edit a paticular index"""
    cpy = list.copy(my_list)
    if idx < 0 or idx >= len(my_list):
        return my_list
    cpy[idx] = element
    return cpy
