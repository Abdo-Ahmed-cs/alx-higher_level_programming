#!/usr/bin/python3
for i in range(26):
    if i % 2 == 1:
        i = i + 32
    print("{}".format(chr(122 - i)), end="")
