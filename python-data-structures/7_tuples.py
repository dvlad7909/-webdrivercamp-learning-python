#!/usr/bin/python3
def tuple_addition(first_tuple=(0, 0), second_tuple=(0, 0)):
    first_list = list(first_tuple)
    second_list = list(second_tuple)
    while len(first_list) < 2:
        first_list.append(0)
    while len(second_list) < 2:
        second_list.append(0)
    res_list = []
    for i in range(0, 2):
        res_list.append(first_list[i] + second_list[i])
    res_tuple = tuple(res_list)
    return res_tuple
