#!/usr/bin/python3


def element_at(my_list, idx):
    """ this function gets the element at an index """
    if idx > len(my_list) or idx < 0:
        return None

    return str(my_list[idx])
