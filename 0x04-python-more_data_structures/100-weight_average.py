#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weights = [pair[1] for pair in my_list]
    scores = list(map(lambda x: x[0] * x[1], my_list))

    sum_of_weights = 0
    sum_of_scores = 0

    for i in scores:
        sum_of_scores += i
    for v in weights:
        sum_of_weights += v
    return sum_of_scores / sum_of_weights
