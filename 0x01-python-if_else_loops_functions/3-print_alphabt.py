#!/usr/bin/python3

for a in range(97, 123):
    if (chr(a) != "q" and chr(a) != "e"):
        print(chr(a), end="")
    a+1
