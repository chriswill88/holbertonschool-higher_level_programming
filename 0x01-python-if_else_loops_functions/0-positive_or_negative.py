#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number == 0:
	is_what="is zero"
elif number > 0:
	is_what="is positive"
else:
	is_what="is negative"
print("{} {}".format(number, is_what))
