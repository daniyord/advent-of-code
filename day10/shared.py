def get_input():
    matrix = []
    trailheads = {}

    with open('input_demo.txt', 'r') as file:
        for i, line in enumerate(file):
            row = []
            matrix.append(row)
            for j, symbol in enumerate(line.strip()):
                row.append(int(symbol))
                if symbol == '0':
                    trailheads[(i, j)] = []

    # for row in matrix:
    #     print(row)

    return (matrix, trailheads)


def find_trailhead_value(trailhead, current, matrix, founds):
    if current == 9:
        founds.append(trailhead)

    i = trailhead[0]
    j = trailhead[1]

    if i >= 1 and matrix[i-1][j] == current+1:
        find_trailhead_value((i-1, j), current+1, matrix, founds)

    if i <= len(matrix)-2 and matrix[i+1][j] == current+1:
        find_trailhead_value((i+1, j), current+1, matrix, founds)

    if j >= 1 and matrix[i][j-1] == current+1:
        find_trailhead_value((i, j-1), current+1, matrix, founds)

    if j <= len(matrix[0])-2 and matrix[i][j+1] == current+1:
        find_trailhead_value((i, j+1), current+1, matrix, founds)
