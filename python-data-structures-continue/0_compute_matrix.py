#!/usr/bin/python3


def compute_matrix(matrix=[]):
    res_matrix = []

    def sq(num):
        return num * num

    for i in matrix:
        j = map(sq, i)
        res_matrix.append(list(j))
    return res_matrix


if __name__ == "__main__":
    matrix = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
    print(f"Original: {matrix}")
    print(f"Modified: {compute_matrix(matrix)}")
