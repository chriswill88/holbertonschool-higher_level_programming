#!/usr/bin/python3


def no_c(my_string):
    """ removes c and C in string and returns it"""
    string = ""  # Declaring a string
    for i in range(len(my_string)):  # Looping through chars in string
        if my_string[i] != 'c' and my_string[i] != 'C':  # No 'c' or 'C'
            string += my_string[i]  # Creating string
    return string  # Returning string
