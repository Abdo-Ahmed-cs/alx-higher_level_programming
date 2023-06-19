#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(1, x + 1):
        try:
            print(my_list[i - 1], end="")
        except IndexError:
            i = i - 1
            break
    print("")
    return i

