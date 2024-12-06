def get_input():
    matrix = []

    with open('input.txt', 'r') as file:
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
