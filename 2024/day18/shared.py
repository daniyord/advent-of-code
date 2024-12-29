def get_input(filename, size, falling):
    file = open(filename, 'r')
    matrix = []
    next_falling = []

    for _ in range(0, size):
        row = []
        matrix.append(row)

        for _ in range(0, size):
            row.append(".")

    for index, line in enumerate(file):
        parts = line.strip().split(",")

        x = int(parts[0])
        y = int(parts[1])

        if index >= falling:
            next_falling.append((x, y))
        else:
            matrix[y][x] = "#"

    return (matrix, next_falling)


def check(matrix, visited, available, total, point, new_x, new_y):
    if new_x < 0 or new_x >= len(matrix):
        return

    if new_y < 0 or new_y >= len(matrix):
        return

    # print(new_x, new_y)

    if matrix[new_y][new_x] == ".":
        next = (new_x, new_y)
        new_total = 1 + total

        if next not in visited or visited[next] > new_total:
            available.add((next, 1 + total))


def short_path(matrix, end):
    visited = {}
    available = {((0, 0), 0)}

    found_min = None
    while len(available) > 0:
        current = None
        for item in available:
            if current is None or item[1] < current[1]:
                current = item

        point = current[0]
        total = current[1]

        available.remove(current)

        if point not in visited or total < visited[point][0]:
            visited[point] = total
        else:
            continue

        x = point[0]
        y = point[1]

        if point == end:
            if found_min is None or total < found_min:
                found_min = total
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

    return found_min
