#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == []:
        return None
    mux = max(a_dictionary.values())
    for k, v in a_dictionary.items():
        if v is mux:
            return k
