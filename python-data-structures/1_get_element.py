#!/usr/bin/python3
def print_element(li, ind):
    if ind < 0 or ind >= len(li):
        return None
    else:
        print(f'The element retrieved is {li[ind]}')


list_ = [5, 4, 3, 2, 1]
index = 2
print_element(list_, index)
