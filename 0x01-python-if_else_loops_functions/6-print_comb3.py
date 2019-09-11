#!/usr/bin/python3

for i in range(0, 9):
	for x in range(0, 9):
		if x > i:
			print("{:02d}".format(i), end = ", ")
