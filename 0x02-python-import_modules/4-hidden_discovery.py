#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    hold = dir(hidden_4)
    length = len(hold)
    for i in range(0, length):
        if hold[i][0] != '_':
            print("{}".format(hold[i]))
    i += 1
