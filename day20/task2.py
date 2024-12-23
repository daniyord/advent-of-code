import sys
sys.path.append('..')

from utils import read_matrix, print_matrix_compact, print_matrix
from shared import find_short_path, restore_paths


def found_connected(max_depth, point, connected):
    visited = set()
    available = [point]
    depth = 1

    while depth <= max_depth:
        new_available = []

        for a in available:
            visited.add(a)

            check(matrix, (a[0] - 1, a[1]), visited,
                  new_available, connected)  # left
            check(matrix, (a[0] + 1, a[1]), visited,
                  new_available, connected)  # right
            check(matrix, (a[0], a[1] - 1), visited,
                  new_available, connected)  # up
            check(matrix, (a[0], a[1] + 1), visited,
                  new_available, connected)  # down

        available = new_available

        # print(f"depth: {depth}")

        depth += 1


def check(matrix, point, visited, available, connected):
    if point[0] == 0 or point[0] >= len(matrix):
        return

    if point[1] == 0 or point[1] >= len(matrix):
        return

    if matrix[point[1]][point[0]] == ".":
        if point[0] < 0:
            print("strange", point, matrix[point[1]][point[0]])
            exit(1)
        connected.add(point)
        return

    if point not in visited:
        available.append(point)


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
    max_depth = 20

    for i, point in enumerate(fpr):
        print(i)

        connected = set()
        found_connected(max_depth, point, connected)

        # print(connected)

        for c in connected:
            if fpr_dict[c] - fpr_dict[point] - 2 >= border:
                result += 1

print(result)
