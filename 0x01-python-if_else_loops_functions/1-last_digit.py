#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    number = number * -1

last = (number % 10)

if last == 0:
    string = "0"
elif last > 5:
    string = "greater than 5"
else:
    string = "less than 6 and not 0"
print("Last digit of {} is {} and is {}".format(number, last, string))
