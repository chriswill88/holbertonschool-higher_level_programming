#!/usr/bin/python3

for i in range(0, 10):
    for x in range(0, 10):
        if x > i:
            print("{:2d}{:d}".format(i, x), end="")
        if x < 10 and i < 8 and x > i:
            print(", ", end="")
print()
