import sys
sys.setrecursionlimit(10**6)
sys.path.append('..')

from utils import print_matrix_compact, print_dict, read_matrix

cache = {}


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
        # print(total)
        # print(path)
        return total

    key = f"{direction}_{x}_{y}"
    # print(path)

    result = -1
    if matrix[y - 1][x] in "SE." and not (x, y - 1) in path:
        if direction == "U":
            result = find_shortest_path(matrix, "U", (x, y - 1),
                                        path, total + 1, totals, depth + 1)
            cache[key] = result

        if direction in "LR":
            result = find_shortest_path(matrix, "U", (x, y - 1),
                                        path, total + 1001, totals, depth + 1)
            cache[key] = result

    if matrix[y + 1][x] in "SE." and not (x, y + 1) in path:
        if direction == "D":
            result = find_shortest_path(matrix, "D", (x, y + 1),
                                        path, total + 1, totals, depth + 1)
            cache[key] = result

        if direction in "LR":
            result = find_shortest_path(matrix, "D", (x, y + 1),
                                        path, total + 1001, totals, depth + 1)
            cache[key] = result

    if matrix[y][x - 1] in "SE." and not (x - 1, y) in path:
        if direction == "L":
            result = find_shortest_path(matrix, "L", (x - 1, y),
                                        path, total + 1, totals, depth + 1)
            cache[key] = result

        if direction in "UD":
            result = find_shortest_path(matrix, "L", (x - 1, y),
                                        path, total + 1001, totals, depth + 1)
            cache[key] = result

    if matrix[y][x + 1] in "SE." and not (x + 1, y) in path:
        if direction == "R":
            result = find_shortest_path(matrix, "R", (x + 1, y),
                                        path, total + 1, totals, depth + 1)
            cache[key] = result

        if direction in "UD":
            result = find_shortest_path(matrix, "R", (x + 1, y),
                                        path, total + 1001, totals, depth + 1)
            cache[key] = result

    return result


matrix, start = get_input("input_demo2.txt")
totals = []

print(f"start: {start}")
print_matrix_compact(matrix)

find_shortest_path(matrix, "R", start, [], 0, totals, 0)

# print(totals)

print_dict(cache)
print("min:", min(totals))
