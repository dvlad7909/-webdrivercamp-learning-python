#!/usr/bin/python3
def not_common_elements(a, b):
    res_set = set()
    for i in a:
        if i not in b:
            res_set.add(i)
        else:
            b.discard(i)
    res_set.update(b)
    return res_set


if __name__ == "__main__":
    set_a = {"API", "requests", "Selenium", "Python", "Behave"}
    set_b = {"Selenium", "Java", "Cucumber", "Maven", "API"}
    elements = not_common_elements(set_a, set_b)
    [print(x) for x in sorted(list(elements))]
