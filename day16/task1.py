import sys
sys.setrecursionlimit(10**6)
sys.path.append('..')

from utils import print_matrix_compact, print_dict, read_matrix

cache = {}


def get_input(filename):
    matrix = []

    file = open(filename, 'r')
    for y, line in enumerate(file):
        row = []
        matrix.append(row)

        for x, symbol in enumerate(line.strip()):
            row.append(symbol)

            if symbol == "S":
                start = (x, y)

    return (matrix, start)


def shortest(matrix, direction, current, path):
    if current in path:
        return -1

    path = path[:]
    path.append(current)

    x = current[0]
    y = current[1]

    if matrix[y][x] not in "SE.":
        return -1

    if matrix[y][x] == "E":
        return 0

    key = f"{direction}_{x}_{y}"

    # if key in path:
    #     return -1

    # path.append(key)

    if key in cache:
        return cache[key]

    results = []
    next = shortest(matrix, "U", (x, y - 1), path)
    if next > -1:
        if direction == "U":
            results.append(1 + next)
        if direction in "LR":
            results.append(1001 + next)

    next = shortest(matrix, "D", (x, y + 1), path)
    if next > -1:
        if direction == "D":
            results.append(1 + next)
        if direction in "LR":
            results.append(1001 + next)

    next = shortest(matrix, "L", (x - 1, y), path)
    if next > -1:
        if direction == "L":
            results.append(1 + next)
        if direction in "UD":
            results.append(1001 + next)

    next = shortest(matrix, "R", (x + 1, y), path)
    if next > -1:
        if direction == "R":
            results.append(1 + next)
        if direction in "UD":
            results.append(1001 + next)

    # print(results)
    if len(results) > 0:
        result = min(results)
        print(result, current, path)
    else:
        result = -1

    cache[key] = result
    return result


matrix, start = get_input("input_demo1.txt")
totals = []

print(f"start: {start}")
print_matrix_compact(matrix)

result = shortest(matrix, "R", start, [])

# print(totals)

# print_dict(cache)
# print("min:", min(totals))

print(result)
