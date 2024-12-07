def get_input():
    matrix = []

    with open('input_demo.txt', 'r') as file:
        for i, line in enumerate(file):
            row = []
            for j, symbol in enumerate(line):
                if symbol != '\n':
                    if symbol == '^':
                        p_x = j
                        p_y = i

                    row.append(symbol)

            matrix.append(row)

    return (matrix, p_x, p_y)


def move(direction, matrix, p_x, p_y):
    match direction:
        case "up":
            return move_up(matrix, p_x, p_y)
        case "right":
            return move_right(matrix, p_x, p_y)
        case "down":
            return move_down(matrix, p_x, p_y)
        case "left":
            return move_left(matrix, p_x, p_y)


def move_up(matrix, p_x, p_y):
    if p_y == 0:
        return ("stop", -1, -1)

    if matrix[p_y - 1][p_x] == "#":
        return ("right", p_x, p_y)
    else:
        return ("move", p_x, p_y - 1)


def move_right(matrix, p_x, p_y):
    if p_x == len(matrix[0]) - 1:
        return ("stop", -1, -1)

    if matrix[p_y][p_x + 1] == "#":
        return ("down", p_x, p_y)
    else:
        return ("move", p_x + 1, p_y)


def move_down(matrix, p_x, p_y):
    if p_y == len(matrix) - 1:
        return ("stop", -1, -1)

    if matrix[p_y + 1][p_x] == "#":
        return ("left", p_x, p_y)
    else:
        return ("move", p_x, p_y + 1)


def move_left(matrix, p_x, p_y):
    if p_x == 0:
        return ("stop", -1, -1)

    if matrix[p_y][p_x - 1] == "#":
        return ("up", p_x, p_y)
    else:
        return ("move", p_x - 1, p_y)
