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


def calculate(filename, correction):
    buttons_A, buttons_B, prizes = read_input(filename, correction)

    result = 0
    for index, prize in enumerate(prizes):
        button_A = buttons_A[index]
        button_B = buttons_B[index]

        y = None
        x = None

        y1 = button_A[0] * prize[1] - button_A[1] * prize[0]
        y2 = button_B[1] * button_A[0] - button_A[1] * button_B[0]

        if y1 % y2 == 0:
            y = y1 // y2

        if y is None:
            continue

        x1 = prize[0] - (button_B[0] * y)
        x2 = button_A[0]

        if x1 % x2 == 0:
            x = x1 // x2

        if x is None:
            continue

        # print(x, y)
        result += 3 * x + y
        # print(result)

    return result
