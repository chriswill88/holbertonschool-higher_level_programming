#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """ this function prints the list """
    for i in range(len(my_list)):  # loop for moving through the list
        str = "{:d}"  # str given a value for str.format
        print(str.format(my_list[i]))  # print using str.format
