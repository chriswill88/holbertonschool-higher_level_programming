#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence is None:
        return (0, None)
    elif sentence is "":
        return (0, "")
    return (len(sentence), sentence[0])
