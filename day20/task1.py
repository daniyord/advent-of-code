import sys
sys.path.append('..')

from utils import read_matrix, print_matrix_compact, print_matrix
from shared import find_short_path, restore_paths


def check_left(i, point, fp):
    for j, check in enumerate(fp[i + 1:]):
        if matrix[point[1]][point[0] - 1] in "E#" and (point[0] - 2, point[1]) == check:
            # print("short_l", point, j - 1)
            return j - 1
    return 0


def check_right(i, point, fp):
    for j, check in enumerate(fp[i + 1:]):
        if matrix[point[1]][point[0] + 1] in "E#" and (point[0] + 2, point[1]) == check:
            # print("short_r", point, j - 1)
            return j - 1
    return 0


def check_up(i, point, fp):
    for j, check in enumerate(fp[i + 1:]):
        if matrix[point[1] - 1][point[0]] in "E#" and (point[0], point[1] - 2) == check:
            # print("short_u", point, j - 1)
            return j - 1
    return 0


def check_down(i, point, fp):
    for j, check in enumerate(fp[i + 1:]):
        if matrix[point[1] + 1][point[0]] in "E#" and (point[0], point[1] + 2) == check:
            # print("short_d", point, j - 1)
            return j - 1
    return 0


matrix, start, end = read_matrix("input.txt")
print_matrix(matrix)

print(start, end)

founded, visited = find_short_path(matrix, start, end)

# print(founded)

founded_paths = restore_paths(visited, founded)

# print()
# print(founded_paths)

# print()

for fp in founded_paths:

    fpr = list(reversed(fp))

    print(len(fp))
    print(fpr)

    result = 0
    border = 100

    for i, point in enumerate(fpr):
        if check_left(i, point, fpr) >= border:
            result += 1

        if check_right(i, point, fpr) >= border:
            result += 1

        if check_up(i, point, fpr) >= border:
            result += 1

        if check_down(i, point, fpr) >= border:
            result += 1

print(result)
