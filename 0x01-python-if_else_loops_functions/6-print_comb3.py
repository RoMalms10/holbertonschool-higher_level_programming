#!/usr/bin/python3
for i in range(0, 9):
	x = i + 1
	if x == 9:
		break
	while (x < 10):
		print("{}{}, ".format(i, x), end="")
		x += 1
print("{}{}".format(i, x))
