#!/usr/bin/python3
my_list = [5, 4, 3, 2, 1]
bool_list = []
for i in my_list:
    if int(i) % 2 == 0:
        bool_list.append(True)
    else:
        bool_list.append(False)
bool_tuple = tuple(bool_list)
print(my_list)
print(bool_tuple)
