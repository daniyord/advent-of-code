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


def next_middle(min, max):
    return min + (max - min) // 2 + (max - min) % 2


def calculate(filename, correction, max_check):
    buttons_A, buttons_B, prizes = read_input(filename, correction)

    result = 0
    for index, prize in enumerate(prizes):
        button_A = buttons_A[index]
        button_B = buttons_B[index]

        min_found = None

        next_i = False

        min_i = 0
        max_i = max_check
        middle_i = next_middle(min_i, max_i)

        min_j = 0
        max_j = max_check
        middle_j = next_middle(min_j, max_j)

        while max_j > min_j:
            value_x = button_A[0] * middle_i + button_B[0] * middle_j
            value_y = button_A[1] * middle_i + button_B[1] * middle_j

            # print(middle, min, max, value_x, value_y, prize)

            if value_x == prize[0] and value_y == prize[1]:
                new_option = 3 * middle_i + middle_j

                if min_found is None or min_found > new_option:
                    min_found = new_option

                break

            if value_x >= prize[0] and value_y < prize[1]:
                next_i = not next_i

            elif value_x > prize[0] and value_y <= prize[1]:
                next_i = not next_i

            elif value_x <= prize[0] and value_y > prize[1]:
                next_i = not next_i

            elif value_x < prize[0] and value_y >= prize[1]:
                next_i = not next_i

            if value_x < prize[0] and value_y < prize[1]:
                if next_i:
                    min_i = middle_i
                else:
                    min_j = middle_j

            if value_x > prize[0] and value_y > prize[1]:
                if next_i:
                    max_i = middle_i
                else:
                    max_j = middle_j

            if next_i:
                middle_i = next_middle(min_i, max_i)
            else:
                middle_j = next_middle(min_j, max_j)

            if middle_i == min_i or middle_i == max_i:
                break

            if middle_j == min_j or middle_j == max_j:
                break

        if min_found is not None:
            result += min_found

    return result
