#!/usr/bin/pyhton3
for i in range(100):
    if i == 99:
        print("99")
        continue
    print("{:02d}".format(i), end=", ")
