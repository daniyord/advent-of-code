def read_matrix(filepath):
    with open(filepath, 'r') as file:
        matrix = []

        for y, line in enumerate(file):
            line = line.strip()

            if (len(line) == 0):
                break

            row = []
            matrix.append(row)

            for x, symbol in enumerate(line):
                if symbol == "S":
                    start = (x, y)
                if symbol == "E":
                    end = (x, y)

                row.append(symbol)

    return (matrix, start, end)


def print_matrix(matrix):
    for line in matrix:
        print(line)


def print_matrix_compact(matrix):
    for line in matrix:
        print("".join(line))


def print_dict(dict):
    for key in dict:
        print(f"{key}: {dict[key]}")
