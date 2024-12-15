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
                    row.append(symbol)

                    if symbol == "@":
                        p_x = j
                        p_y = i

                # print(line)

            if matrix_ended:
                commands += line

    return (matrix, p_x, p_y, commands)
