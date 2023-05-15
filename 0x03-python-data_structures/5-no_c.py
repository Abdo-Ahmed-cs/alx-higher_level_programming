#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    if my_string is None:
        return
    else:
        for i in range(0, len(my_string)):
            if my_string[i] not in "cC":
                new_string = new_string + my_string[i]
        return new_string
