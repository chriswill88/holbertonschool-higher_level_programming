#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    lis = []
    for i in range(list_length):
        try:
            x = my_list_1[i]
            y = my_list_2[i]
            div = x / y
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
        finally:
            lis.append(div)
    return lis
