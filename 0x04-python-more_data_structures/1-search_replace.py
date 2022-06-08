#!/usr/bin/python3
def search_replace(my_list, search, replace):
    swap_list = []
    for i in my_list:
        if i == search:
            swap_list.append(replace)
        else:
            swap_list.append(i)
    return swap_list
