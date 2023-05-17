#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    else:
        best_score_v = a_dictionary[next(iter(a_dictionary))]
        for k, v in a_dictionary.items():
            if best_score_v < v:
                best_score_v = v
        keys = [key for key, value in a_dictionary.items()
                if value == best_score_v]
        return keys[0]
