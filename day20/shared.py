def check_next(matrix, x_corection, y_corection, next, visited, available):
    x = next[0][0]
    y = next[0][1]
    total = next[1]

    if matrix[y + y_corection][x + x_corection] in "E.":
        new_point = (x + x_corection, y + y_corection)

        if new_point not in visited:
            if new_point not in available or available[new_point][0] > total + 1:
                available[new_point] = (total + 1, {(x, y)})
            elif available[new_point][0] == total + 1:
                available[new_point][1].add((x, y))


def find_short_path(matrix, start, end):
    visited = {}
    available = {start: (0, set())}
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
        elif visited[(x, y)][0] == total:
            visited[(x, y)][1].insert(prev)

        if (next[0] == end):
            print("success", available[key][0])

            founded = (key, (available[key][1]))

            del available[next[0]]
            continue

        check_next(matrix, 0, -1, next, visited, available)  # up
        check_next(matrix, 0, 1, next, visited, available)  # down
        check_next(matrix, -1, 0, next, visited, available)  # left
        check_next(matrix, 1, 0, next, visited, available)  # right

        del available[next[0]]

    return (founded, visited)


def restore_paths(visited, prev):
    print("restore_paths", prev)

    result = []

    for prev_option in prev[1]:
        print([prev[0]])
        print(visited[prev_option][1])
        result.append([prev[0]] + [prev_option])

    while True:
        # print("while")

        # print(result)

        new_result = []

        for item in result:
            # print(item[-1])
            next = visited[item[-1]]
            # print(next)

            if len(next[1]) == 0:
                break

            for n in next[1]:
                new_result.append(item + [n])

        if len(new_result) == 0:
            break
        else:
            result = new_result

    return result
