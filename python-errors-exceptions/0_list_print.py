#!/usr/bin/python3
def list_print(lst=[], i=0):
    count_items = 0
    for x in range(0, i):
        try:
            print(lst[x], end='')
            count_items += 1
        except:
            break
    print()
    return count_items


if __name__ == "__main__":
    list_ = [1, 2, 3, 4, 5, 6, 7]

    count = list_print(list_, 4)
    print(f"Count: {count:d}")
    count = list_print(list_, len(list_))
    print(f"Count: {count:d}")
    count = list_print(list_, len(list_) + 2)
    print(f"Count: {count:d}")
