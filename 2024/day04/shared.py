def get_input():
    matrix = []

    with open('input.txt', 'r') as file:
        for line in file:
            row = []
            for symbol in line:
                if symbol != '\n':
                    row.append(symbol)

            matrix.append(row)

    return matrix
