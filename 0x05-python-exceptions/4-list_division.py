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
        except:
            if y == 0:
                print("division by zero")
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
            elif isinstance(y, (int, float) or isinstance(x, (int, float))):
                print("wrong type")
            div = 0
        finally:
            lis.append(div)
    return lis
