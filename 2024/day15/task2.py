import sys
sys.path.append('..')

from utils import print_matrix_compact, print_dict, read_matrix


def get_input(filename):
    matrix_ended = False
    commands = ""
    matrix = []

    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            line = line.strip()

            if len(line) == 0:
                matrix_ended = True

            if not matrix_ended:
                row = []
                matrix.append(row)

                for j, symbol in enumerate(line):
                    match symbol:
                        case "#":
                            row.append("#")
                            row.append("#")
                        case "O":
                            row.append("[")
                            row.append("]")
                        case ".":
                            row.append(".")
                            row.append(".")
                        case "@":
                            row.append("@")
                            row.append(".")

                    if symbol == "@":
                        p_x = j * 2
                        p_y = i

            if matrix_ended:
                commands += line

    return (matrix, p_x, p_y, commands)


def exec_command(command, matrix, p_x, p_y):
    match command:
        case ">":
            return exec_right(matrix, p_x, p_y)
        case "<":
            return exec_left(matrix, p_x, p_y)
        case "^":
            return exec_up(matrix, p_x, p_y)
        case "v":
            return exec_down(matrix, p_x, p_y)


def exec_right(matrix, p_x, p_y):
    x = p_x
    y = p_y

    while matrix[y][x] not in "#.":
        x += 1

    if matrix[y][x] == ".":
        for i in range(x, p_x, -1):
            matrix[y][i] = matrix[y][i - 1]
        matrix[p_y][p_x] = "."
        return (p_x + 1, p_y)

    return (p_x, p_y)


def exec_left(matrix, p_x, p_y):
    x = p_x
    y = p_y

    while matrix[y][x] not in "#.":
        x -= 1

    if matrix[y][x] == ".":
        for i in range(x, p_x, 1):
            matrix[y][i] = matrix[y][i + 1]
        matrix[p_y][p_x] = "."
        return (p_x - 1, p_y)

    return (p_x, p_y)


def exec_up(matrix, p_x, p_y):
    x = p_x
    y = p_y

    print(x, y)

    if matrix[y - 1][x] == "#":
        return (p_x, p_y)

    if matrix[y - 1][x] == ".":
        matrix[p_y - 1][p_x] = "@"
        matrix[p_y][p_x] = "."
        return (p_x, p_y - 1)

    upper_lines = []
    y -= 1

    if matrix[y][x] == "[":
        upper_line = {(x, y, "["), (x + 1, y, "]")}

    if matrix[y][x] == "]":
        upper_line = {(x - 1, y, "["), (x, y, "]")}

    upper_lines.append(upper_line)

    may_move = False
    must_stop = False
    while not may_move and not must_stop:
        last_upper_line = upper_lines[-1]

        upper_line = set()

        y -= 1

        may_move = True
        for p in last_upper_line:
            if matrix[y][p[0]] != ".":
                may_move = False

        for p in last_upper_line:
            if matrix[y][p[0]] == "#":
                must_stop = True
                break
            if matrix[y][p[0]] == "[":
                upper_line.add((p[0], y, "["))
                upper_line.add((p[0] + 1, y, "]"))
            if matrix[y][p[0]] == "]":
                upper_line.add((p[0] - 1, y, "["))
                upper_line.add((p[0], y, "]"))

        if len(upper_line) > 0:
            upper_lines.append(upper_line)

    print(upper_lines, may_move, must_stop)

    if may_move and not must_stop:
        # print(upper_lines)

        for upper_line in reversed(upper_lines):
            for p in upper_line:
                matrix[p[1] - 1][p[0]] = p[2]
                matrix[p[1]][p[0]] = "."

        matrix[p_y - 1][p_x] = "@"
        matrix[p_y][p_x] = "."
        return (p_x, p_y - 1)

    return (p_x, p_y)


def exec_down(matrix, p_x, p_y):
    x = p_x
    y = p_y

    if matrix[y + 1][x] == "#":
        return (p_x, p_y)

    if matrix[y + 1][x] == ".":
        matrix[p_y + 1][p_x] = "@"
        matrix[p_y][p_x] = "."
        return (p_x, p_y + 1)

    downer_lines = []
    y += 1

    if matrix[y][x] not in "[]":
        print(matrix[y][x])
        exit(10)

    if matrix[y][x] == "[":
        downer_line = {(x, y, "["), (x + 1, y, "]")}

    if matrix[y][x] == "]":
        downer_line = {(x - 1, y, "["), (x, y, "]")}

    downer_lines.append(downer_line)

    may_move = False
    must_stop = False
    while not may_move and not must_stop:
        last_downer_line = downer_lines[-1]

        downer_line = set()

        y += 1

        may_move = True
        for p in last_downer_line:
            if matrix[y][p[0]] != ".":
                may_move = False

        for p in last_downer_line:
            if matrix[y][p[0]] == "#":
                must_stop = True
                break
            if matrix[y][p[0]] == "[":
                downer_line.add((p[0], y, "["))
                downer_line.add((p[0] + 1, y, "]"))
            if matrix[y][p[0]] == "]":
                downer_line.add((p[0] - 1, y, "["))
                downer_line.add((p[0], y, "]"))

        if len(downer_line) > 0:
            downer_lines.append(downer_line)

    if may_move and not must_stop:
        # print(upper_lines)

        for downer_line in reversed(downer_lines):
            for p in downer_line:
                matrix[p[1] + 1][p[0]] = p[2]
                matrix[p[1]][p[0]] = "."

        matrix[p_y + 1][p_x] = "@"
        matrix[p_y][p_x] = "."
        return (p_x, p_y + 1)

    return (p_x, p_y)


matrix, p_x, p_y, commands = get_input("input.txt")

# print(p_x, p_y)
# print_matrix_compact(matrix)
# print(commands)
# exit(0)

for command in commands:
    print()
    print(command)
    p_x, p_y = exec_command(command, matrix, p_x, p_y)
    # print_matrix_compact(matrix)

# print_matrix_compact(matrix)


result = 0
for y, row in enumerate(matrix):
    for x, _ in enumerate(row):
        if matrix[y][x] == "[":
            result += (y * 100 + x)

print(result)
