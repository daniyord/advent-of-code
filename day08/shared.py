def get_input():
    matrix = []
    antenas = {}

    with open('input.txt', 'r') as file:
        for i, line in enumerate(file):
            row = []
            for j, symbol in enumerate(line):
                if symbol != '\n':
                    row.append(symbol)

                    if symbol != ".":
                        if symbol not in antenas:
                            antenas[symbol] = []

                        antenas[symbol].append((i, j))

            matrix.append(row)

    return matrix, antenas
