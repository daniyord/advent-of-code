import sys
sys.path.append('..')

from utils import print_matrix_compact, print_dict, read_matrix
from shared import get_input


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

    while matrix[y][x] not in "#.":
        y -= 1

    if matrix[y][x] == ".":
        for i in range(y, p_y, 1):
            matrix[i][x] = matrix[i + 1][x]
        matrix[p_y][p_x] = "."
        return (p_x, p_y - 1)

    return (p_x, p_y)


def exec_down(matrix, p_x, p_y):
    x = p_x
    y = p_y

    while matrix[y][x] not in "#.":
        y += 1

    if matrix[y][x] == ".":
        for i in range(y, p_y, -1):
            matrix[i][x] = matrix[i - 1][x]
        matrix[p_y][p_x] = "."
        return (p_x, p_y + 1)

    return (p_x, p_y)


matrix, p_x, p_y, commands = get_input("input.txt")

# print(p_x, p_y)
# print_matrix_compact(matrix)
# print(commands)


for command in commands:
    # print()
    # print(command)
    p_x, p_y = exec_command(command, matrix, p_x, p_y)
    # print_matrix_compact(matrix)

print_matrix_compact(matrix)


result = 0
for y, row in enumerate(matrix):
    for x, _ in enumerate(row):
        if matrix[y][x] == "O":
            result += (y * 100 + x)

print(result)
