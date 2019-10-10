#!/usr/bin/python3
def best_score(a_dictionary):
    i = 0
    try:
        for x, y in a_dictionary.items():
            if y >= i:
                i = y
                hold = x
    except:
        return None
    return hold
