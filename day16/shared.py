import sys
sys.path.append('..')

from utils import print_dict


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


def check(matrix, visited, total, direction, new_x, new_y, new_direction, limit_direction, turn_directions):
    if matrix[new_y][new_x] in "E." and direction != limit_direction:
        next = (new_x, new_y, new_direction)

        if direction == new_direction:
            new_total = 1 + total
        if direction in turn_directions:
            new_total = 1001 + total

        if next not in visited or visited[next][0] > new_total:
            return (next, new_total)

    return None


def shortest_path(matrix, start):
    visited = {}
    available = {(start, (0, None))}

    found = None
    found_min = None
    while len(available) > 0:
        current = None
        for item in available:
            if current is None or item[1][0] < current[1][0]:
                current = item

        available.remove(current)

        if current[0] not in visited or current[1][0] < visited[current[0]][0]:
            visited[current[0]] = (
                current[1][0], None if current[1][1] is None else [current[1][1]])
        elif current[1][0] == visited[current[0]][0]:
            visited[current[0]][1].append(current[1][1])

        x = current[0][0]
        y = current[0][1]
        direction = current[0][2]
        total = current[1][0]

        if matrix[y][x] == "E":
            # print("available:", available)
            # print("visited:", visited)
            if found_min is None or current[1][0] < found_min:
                found = [current[0]]
                found_min = current[1][0]
            elif found_min == current[1][0]:
                found.append(current[0])

        up = check(matrix, visited, total, direction, x, y - 1, "U", "D", "LR")
        if up:
            available.add((up[0], (up[1], current[0])))

        down = check(matrix, visited, total, direction,
                     x, y + 1, "D", "U", "LR")
        if down:
            available.add((down[0], (down[1], current[0])))

        left = check(matrix, visited, total, direction,
                     x - 1, y, "L", "R", "UD")
        if left:
            available.add((left[0], (left[1], current[0])))

        right = check(matrix, visited, total, direction,
                      x + 1, y, "R", "L", "UD")
        if right:
            available.add((right[0], (right[1], current[0])))

    return found_min, found, visited
