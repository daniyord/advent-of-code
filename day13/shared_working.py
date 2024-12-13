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
        for i in range(0, max_check + 1):
            min = 0
            max = max_check
            middle = next_middle(min, max)

            while max > min:
                value_x = button_A[0] * i + button_B[0] * middle
                value_y = button_A[1] * i + button_B[1] * middle

                # print(middle, min, max, value_x, value_y, prize)

                if value_x >= prize[0] and value_y < prize[1]:
                    break

                if value_x > prize[0] and value_y <= prize[1]:
                    break

                if value_x <= prize[0] and value_y > prize[1]:
                    break

                if value_x < prize[0] and value_y >= prize[1]:
                    break

                if value_x == prize[0] and value_y == prize[1]:
                    new_option = 3 * i + middle

                    if min_found is None or min_found > new_option:
                        min_found = new_option

                    break

                if value_x < prize[0] and value_y < prize[1]:
                    min = middle

                if value_x > prize[0] and value_y > prize[1]:
                    max = middle

                middle = next_middle(min, max)

                if middle == min or middle == max:
                    break

        if min_found is not None:
            result += min_found

    return result
