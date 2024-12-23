import sys
sys.path.append('..')

from utils import read_matrix, print_matrix_compact, print_matrix
from shared import find_short_path, restore_paths


def check_left(i, point, fp):
    new_point = point[0] - 2, point[1]
    if matrix[point[1]][point[0] - 1] in "E#" and new_point in fp and fp[new_point] > i:
        return fp[new_point] - i - 1

    return 0


def check_right(i, point, fp):
    new_point = point[0] + 2, point[1]
    if matrix[point[1]][point[0] + 1] in "E#" and new_point in fp and fp[new_point] > i:
        return fp[new_point] - fp[point] - 2

    return 0


def check_up(i, point, fp):
    new_point = point[0], point[1] - 2
    if matrix[point[1] - 1][point[0]] in "E#" and new_point in fp and fp[new_point] > i:
        return fp[new_point] - fp[point] - 2

    return 0


def check_down(i, point, fp):
    new_point = point[0], point[1] + 2
    if matrix[point[1] + 1][point[0]] in "E#" and new_point in fp and fp[new_point] > i:
        return fp[new_point] - fp[point] - 2

    return 0


matrix, start, end = read_matrix("input.txt")

founded, visited = find_short_path(matrix, start, end)

founded_paths = restore_paths(visited, founded)


result = 0
for fp in founded_paths:

    fpr = list(reversed(fp))

    fpr_dict = {}
    for index, fp in enumerate(fpr):
        fpr_dict[fp] = index

    border = 100

    for i, point in enumerate(fpr):
        if check_left(i, point, fpr_dict) >= border:
            result += 1

        if check_right(i, point, fpr_dict) >= border:
            result += 1

        if check_up(i, point, fpr_dict) >= border:
            result += 1

        if check_down(i, point, fpr_dict) >= border:
            result += 1

print(result)

# 1411
