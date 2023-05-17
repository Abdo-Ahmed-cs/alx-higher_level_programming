#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_set_1 = list(filter(lambda x: x not in set_2, set_1))
    diff_set_2 = list(filter(lambda y: y not in set_1, set_2))
    diff_set_1.extend(diff_set_2)
    return diff_set_1
