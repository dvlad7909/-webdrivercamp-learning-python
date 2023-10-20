#!/usr/bin/python3
def print_replaced_element(li, ind, el):
    li_origin = li.copy()
    if ind < 0 or ind >= len(li):
        print(li_origin)
    else:
        li[ind] = el
        print(f'Copy:     {li}')
        print(f'Original: {li_origin}')


list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5
print_replaced_element(list_, index, element_to_replace)
