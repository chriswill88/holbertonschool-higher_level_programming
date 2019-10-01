#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    lis = []
    l1 = len(my_list_1)
    l2 = len(my_list_2)
    if (l1 > l2):
        l2 = l1
    for i in range(l2):
        try:
            x = my_list_1[i]
            y = my_list_2[i]
            div = x / y
        except ZeroDivisionError:
            print("division by zero")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            lis.append(div)
    return lis
