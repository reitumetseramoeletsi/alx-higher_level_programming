#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    i = 0

    for val in my_list:
        if val % 2 == 0:
            new_list[i] = True
            i += 1
        else:
            new_list[i] = False
            i += 1
    return new_list
