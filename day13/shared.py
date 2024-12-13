import sys
sys.path.append('..')

from utils import print_matrix, print_dict, read_matrix
# from shared import prepare_input


def parse_button(line):
    parts = line.split(":")[1].replace("X+", "").replace("Y+", "").split(",")

    return (int(parts[0]), int(parts[1]))


def parse_prize(line, correction):
    parts = line.split(":")[1].replace("X=", "").replace("Y=", "").split(",")

    return (int(parts[0]) + correction, int(parts[1]) + correction)


def read_input(filepath, correction):
    with open(filepath, 'r') as file:
        buttons_A = []
        buttons_B = []
        prizes = []

        for index, line in enumerate(file):
            if index % 4 == 0:
                # print("buttonA:", line.strip())
                buttons_A.append(parse_button(line.strip()))

            if index % 4 == 1:
                # print("buttonB:", line.strip())
                buttons_B.append(parse_button(line.strip()))

            if index % 4 == 2:
                # print("prize:", line.strip())
                prizes.append(parse_prize(line.strip(), correction))

    return (buttons_A, buttons_B, prizes)


def prepare_cache(cache, value, max_check):
    if value in cache:
        return

    cached_data = [0]
    current = 0
    for _ in range(0, max_check):
        current += value
        cached_data.append(current)

    cache[value] = cached_data


def calculate(filename, correction, max_check):
    cache = {}

    buttons_A, buttons_B, prizes = read_input(filename, correction)

    result = 0
    for index, prize in enumerate(prizes):
        button_A = buttons_A[index]
        button_B = buttons_B[index]

        prepare_cache(cache, button_A[0], max_check)
        prepare_cache(cache, button_A[1], max_check)
        prepare_cache(cache, button_B[0], max_check)
        prepare_cache(cache, button_B[1], max_check)

        min = None
        for i in range(0, max_check + 1):
            for j in range(0, max_check + 1):
                value_x = cache[button_A[0]][i] + cache[button_B[0]][j]
                value_y = cache[button_A[1]][i] + cache[button_B[1]][j]

                # print(value_x)

                if value_x == prize[0] and value_y == prize[1]:
                    new_option = 3 * i + j
                    # print(button_A, button_B, i, j)

                    if min is None or min > new_option:
                        min = new_option

                # if value_x > prize[0] or value_y > prize[1]:
                #     break

        if min is not None:
            result += min

    return result
