import sys
sys.path.append('..')

from utils import print_matrix_compact, print_dict


def get_input(filename, size, falling):
    file = open(filename, 'r')
    matrix = []

    for _ in range(0, size):
        row = []
        matrix.append(row)

        for _ in range(0, size):
            row.append(".")

    for index, line in enumerate(file):
        if index >= falling:
            break

        parts = line.strip().split(",")

        x = int(parts[0])
        y = int(parts[1])

        # print(x, y)

        matrix[y][x] = "#"

    return matrix


def check(matrix, visited, available, total, point, new_x, new_y):
    if new_x < 0 or new_x >= len(matrix):
        return

    if new_y < 0 or new_y >= len(matrix):
        return

    # print(new_x, new_y)

    if matrix[new_y][new_x] == ".":
        next = (new_x, new_y)
        new_total = 1 + total

        if next not in visited or visited[next][0] > new_total:
            available.add((next, (1 + total, point)))


def short_path(matrix, end):
    visited = {}
    available = {((0, 0), (0, None))}

    found = None
    found_min = None
    while len(available) > 0:
        current = None
        for item in available:
            if current is None or item[1][0] < current[1][0]:
                current = item

        point = current[0]
        total = current[1][0]
        prev = current[1][1]

        available.remove(current)

        if point not in visited or total < visited[point][0]:
            visited[point] = (total, [prev])
        elif total == visited[point][0]:
            visited[point][1].append(prev)
        else:
            continue

        x = point[0]
        y = point[1]

        if point == end:
            if found_min is None or total < found_min:
                found = [point]
                found_min = total
            elif found_min == total:
                found.append(point)
            else:
                continue

        check(matrix, visited, available, total, point, x, y - 1)  # up
        check(matrix, visited, available, total, point, x, y + 1)  # down
        check(matrix, visited, available, total, point, x - 1, y)  # left
        check(matrix, visited, available, total, point, x + 1, y)  # right

        # print(f"available: {available}")
        # print(f"visited: {visited}")
        # print()
        # input()

    return found_min, found, visited


# matrix = get_input("input_demo.txt", 7, 12)
# found_min, _, _ = short_path(matrix, (6, 6))

matrix = get_input("input.txt", 71, 1024)
found_min, _, _ = short_path(matrix, (70, 70))

# print_matrix_compact(matrix)


print(found_min)
