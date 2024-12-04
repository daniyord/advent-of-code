def get_data():
    matrix = []

    with open('input_demo.txt', 'r') as file:
        for line in file:
            row = []
            for symbol in line:
                if symbol != '\n':
                    row.append(symbol)

            matrix.append(row)

    return matrix


def check_field(matrix, x, y):
    if y < len(matrix[0]) - 3:
        if matrix[x][y] == "X" and matrix[x][y+1] == "M" and matrix[x][y+2] == "A" and matrix[x][y+3] == "S":
            return True

        if matrix[x][y] == "S" and matrix[x][y+1] == "A" and matrix[x][y+2] == "M" and matrix[x][y+3] == "X":
            return True

    if x < len(matrix) - 3:
        if matrix[x][y] == "X" and matrix[x+1][y] == "M" and matrix[x+2][y] == "A" and matrix[x+3][y] == "S":
            return True

        if matrix[x][y] == "S" and matrix[x+1][y] == "A" and matrix[x+2][y] == "M" and matrix[x+3][y] == "X":
            return True

    if x < len(matrix) - 3 and y < len(matrix[0]) - 3:
        if matrix[x][y] == "X" and matrix[x+1][y+1] == "M" and matrix[x+2][y+2] == "A" and matrix[x+3][y+3] == "S":
            return True

        if matrix[x][y] == "S" and matrix[x+1][y+1] == "A" and matrix[x+2][y+2] == "M" and matrix[x+3][y+3] == "X":
            return True

    if x >= 3 and y < len(matrix[0]) - 3:
        if matrix[x][y] == "X" and matrix[x-1][y+1] == "M" and matrix[x-2][y+2] == "A" and matrix[x-3][y+3] == "S":
            return True

        if matrix[x][y] == "S" and matrix[x-1][y+1] == "A" and matrix[x-2][y+2] == "M" and matrix[x-3][y+3] == "X":
            return True

    return False


matrix = get_data()

result = 0

for i, row in enumerate(matrix):
    for j, cell in enumerate(row):
        if check_field(matrix, i, j):
            result += 1

print(result)
