#!/usr/bin/python3
for i in range(122, 96, -1):
    alter = i
    if alter % 2 != 0:
        alter -= 32
    print("{}".format(chr(alter)), end="")
