#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if (ord(ch) > ord("Z")):
            ch = chr(ord(ch) - 32)
        print("{}".format(ch), end="")
    print("")
