import sys
sys.setrecursionlimit(10**4)
sys.path.append('..')

from utils import print_matrix_compact, print_dict, read_matrix


def get_input(filename):
    matrix = []

    with open(filename, 'r') as file:
        for y, line in enumerate(file):
            row = []
            matrix.append(row)

            for x, symbol in enumerate(line.strip()):
                row.append(symbol)

                if symbol == "S":
                    start = (x, y)

    return (matrix, start)


def find_shortest_path(matrix, direction, current, path, total, totals, depth):

    # if depth > 200:
    #     print(path)
    #     print(current)
    #     exit(0)
    #     return

    # print(direction, current)

    path = path[:]
    # print(path)
    path.append(current)
    # print(path)

    x = current[0]
    y = current[1]

    # print(y, x, matrix[y][x])

    if matrix[y][x] == "E":
        # print(total, path)
        totals.append(total)
        return

    # print(path)
    if matrix[y - 1][x] in "SE." and not (x, y - 1) in path:
        if direction == "U":
            find_shortest_path(matrix, "U", (x, y - 1),
                               path, total + 1, totals, depth + 1)
        if direction in "LR":
            find_shortest_path(matrix, "U", (x, y - 1),
                               path, total + 1001, totals, depth + 1)

    if matrix[y + 1][x] in "SE." and not (x, y + 1) in path:
        if direction == "D":
            find_shortest_path(matrix, "D", (x, y + 1),
                               path, total + 1, totals, depth + 1)
        if direction in "LR":
            find_shortest_path(matrix, "D", (x, y + 1),
                               path, total + 1001, totals, depth + 1)

    if matrix[y][x - 1] in "SE." and not (x - 1, y) in path:
        if direction == "L":
            find_shortest_path(matrix, "L", (x - 1, y),
                               path, total + 1, totals, depth + 1)
        if direction in "UD":
            find_shortest_path(matrix, "L", (x - 1, y),
                               path, total + 1001, totals, depth + 1)

    if matrix[y][x + 1] in "SE." and not (x + 1, y) in path:
        if direction == "R":
            find_shortest_path(matrix, "R", (x + 1, y),
                               path, total + 1, totals, depth + 1)
        if direction in "UD":
            find_shortest_path(matrix, "R", (x + 1, y),
                               path, total + 1001, totals, depth + 1)


matrix, start = get_input("input.txt")
totals = []

print(f"start: {start}")
print_matrix_compact(matrix)

find_shortest_path(matrix, "R", start, [], 0, totals, 0)

print(totals)

print(min(totals))
