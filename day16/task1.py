import sys
sys.setrecursionlimit(10**6)
sys.path.append('..')

from utils import print_matrix_compact, print_dict, read_matrix


def get_input(filename):
    matrix = []

    file = open(filename, 'r')
    for y, line in enumerate(file):
        row = []
        matrix.append(row)

        for x, symbol in enumerate(line.strip()):
            row.append(symbol)

            if symbol == "S":
                start = (x, y, "R")

    return (matrix, start)


def check(matrix, total, new_x, new_y, new_direction, limit_direction, turn_directions):
    if matrix[new_y][new_x] in "E." and direction != limit_direction:
        next = (new_x, new_y, new_direction)

        if direction == new_direction:
            new_total = 1 + total
        if direction in turn_directions:
            new_total = 1001 + total

        # if next in visited:
        #     print(visited[next], new_total)
        if next not in visited or visited[next][0] > new_total:
            return (next, new_total)

    return None


matrix, start = get_input("input.txt")
totals = []

print(f"start: {start}")
print_matrix_compact(matrix)

visited = {}
available = {(start, (0, None))}

# print("available:", available)
# print("visited:", visited)

found = None
depth = 0
while len(available) > 0:
    # current = available[0]

    # for i in range(1, len(available)):
    #     if available[i][1][0] < current[1][0]:
    #         current = available[i]

    current = None
    for item in available:
        if current is None or item[1][0] < current[1][0]:
            current = item

    available.remove(current)
    visited[current[0]] = current[1]

    x = current[0][0]
    y = current[0][1]
    direction = current[0][2]
    total = current[1][0]

    if matrix[y][x] == "E":
        found = current[1][0]
        # print("available:", available)
        # print("visited:", visited)
        print(found)
        # exit(0)

    # print(f"{depth}: available: {len(available)} visited: {
    #       len(visited)} current: {current}")

    up = check(matrix, total, x, y - 1, "U", "D", "LR")
    if up:
        available.add((up[0], (up[1], current[0])))

    down = check(matrix, total, x, y + 1, "D", "U", "LR")
    if down:
        available.add((down[0], (down[1], current[0])))

    left = check(matrix, total, x - 1, y, "L", "R", "UD")
    if left:
        available.add((left[0], (left[1], current[0])))

    right = check(matrix, total, x + 1, y, "R", "L", "UD")
    if right:
        available.add((right[0], (right[1], current[0])))

    # print(f"{depth}: available: {len(available)} visited: {
    #       len(visited)} current: {current}")

    # print()
    # print("available:", available)
    # print("visited:", visited)

    depth += 1
