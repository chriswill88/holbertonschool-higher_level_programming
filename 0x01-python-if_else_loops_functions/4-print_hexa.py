#!/usr/bin/python3
x = 0
it = 0
asci = 97
for i in range(0, 98):

    if x == 15:
        asci = 97
        x = 0
        it = it + 1
    else:
        x = x + 1
    if x > 9:
        char = chr(asci)
        asci = asci + 1
    else:
        char = x
        i = i + 1

    print("{} = {}x{}{}".format(i, 0, it, char))
