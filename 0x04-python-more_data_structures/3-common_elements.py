#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_list = list(filter(lambda x: x in set_2, set_1))
    return common_list
