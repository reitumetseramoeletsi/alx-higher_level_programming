#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == {}:
        return (0)
    mark1 = 0
    mark2 = 0
    for x, y in my_list:
        mark1 += x * y
        mark2 += y
    return (mark1 / mark2)
