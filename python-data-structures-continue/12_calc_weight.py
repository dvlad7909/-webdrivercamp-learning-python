#!/usr/bin/python3
def calc_weight(list_=[]):
    if len(list_) == 0:
        return 0
    else:
        numer = 0
        denom = 0
        for i in list_:
            a, b = i
            numer += a * b
            denom += b
        return numer / denom


if __name__ == "__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")
