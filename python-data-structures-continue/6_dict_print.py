#!/usr/bin/python3
def dict_print(dict_):
    key_list = sorted(dict_)
    for i in key_list:
        print(f'{i}: {dict_[i]}')


if __name__ == "__main__":
    dict_ = {
            "libs": (1, 2, 3),
            "x": "Selenium",
            "lang": ["Java", "Python"],
            "frame": "Behave",
            "set": set()
            }
    dict_print(dict_)
