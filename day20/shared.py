import sys
sys.path.append('..')

from utils import read_matrix, print_matrix_compact, print_matrix, print_dict


def check_next(matrix, x_corection, y_corection, next, visited, available):
    x = next[0][0]
    y = next[0][1]
    total = next[1]

    if matrix[y + y_corection][x + x_corection] in "E.":
        new_point = (x + x_corection, y + y_corection)

        if new_point not in visited:
            if new_point not in available or available[new_point][0] > total + 1:
                available[new_point] = (total + 1, (x, y))


def find_short_path(matrix, start, end):
    visited = {}
    available = {start: (0, None)}
    founded = []

    while len(available) > 0:
        next = None

        for key in available:
            if next is None or available[key][0] < next[1]:
                next = (key, available[key][0], available[key][1])

        x = next[0][0]
        y = next[0][1]
        total = next[1]
        prev = next[2]

        if (x, y) not in visited or visited[(x, y)][0] > total:
            visited[(x, y)] = (total, prev)

        if (next[0] == end):
            founded = (key, available[key][1])

            del available[next[0]]
            continue

        check_next(matrix, 0, -1, next, visited, available)  # up
        check_next(matrix, 0, 1, next, visited, available)  # down
        check_next(matrix, -1, 0, next, visited, available)  # left
        check_next(matrix, 1, 0, next, visited, available)  # right

        del available[next[0]]

    return (founded, visited)


def restore_path(visited, prev):
    result = []

    while prev[1] != None:
        result.append(prev[0])
        prev = (prev[1], visited[prev[1]][1])

    return result


def process(filename, min_advancement, cheat):
    matrix, start, end = read_matrix(filename)

    founded, visited = find_short_path(matrix, start, end)
    founded_path = restore_path(visited, founded) + [start]

    founded_path = list(reversed(founded_path))

    # print(len(founded_path))
    # print(founded_path)

    total = len(founded_path)

    result = 0
    result_dict = {}
    total = len(founded_path)

    for i in range(0, len(founded_path)):
        for j in range(i + 1, len(founded_path)):
            first = founded_path[i]
            second = founded_path[j]

            first_to_end = total - i
            second_to_end = total - j
            first_to_second = first_to_end - second_to_end
            manhatan = abs(first[0] - second[0]) + abs(first[1] - second[1])

            if manhatan <= cheat:
                diff = first_to_second - manhatan
                if diff >= min_advancement:
                    if diff not in result_dict:
                        result_dict[diff] = 0
                    result_dict[diff] += 1

                    result += 1

    # print_dict(result_dict)

    return result
