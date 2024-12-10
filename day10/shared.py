def get_input():
    matrix = []
    trailheads = {}

    with open('input.txt', 'r') as file:
        for i, line in enumerate(file):
            row = []
            matrix.append(row)
            for j, symbol in enumerate(line.strip()):
                row.append(int(symbol))
                if symbol == '0':
                    trailheads[(i, j)] = set()

    return (matrix, trailheads)


def print_matrix(matrix):
    for row in matrix:
        print(row)
