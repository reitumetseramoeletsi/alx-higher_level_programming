#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy_d = a_dictionary.copy()

    for k in copy_d:
        copy_d[k] *= 2
    return copy_d
