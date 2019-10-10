#!/usr/bin/python3


def roman_to_int(roman_string):
    rs = roman_string
    num = 0
    romnum = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    if not isinstance(roman_string, (str)) or roman_string is None:
        return 0
    for x in range(len(rs)):
        for key, val in romnum.items():
            if rs[x] is key:
                if key is 'I' and x + 1 < len(rs) and rs[x + 1] is not 'I':
                    num -= val
                else:
                    num += val

    return num
