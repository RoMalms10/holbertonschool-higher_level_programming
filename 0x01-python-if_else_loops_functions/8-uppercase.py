#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        check = ord(str[i])
        if check >= 97 and check <= 122:
            check -= 32
        check = chr(check)
        print("{}".format(check), end="")
    print("")
