from shared import get_input


def check_field(matrix, x, y):
    len_x = len(matrix)
    len_y = len(matrix[0])

    count = 0

    if y <= len_y - 4:
        if matrix[x][y] == "X" and matrix[x][y+1] == "M" and matrix[x][y+2] == "A" and matrix[x][y+3] == "S":
            count += 1

        if matrix[x][y] == "S" and matrix[x][y+1] == "A" and matrix[x][y+2] == "M" and matrix[x][y+3] == "X":
            count += 1

    if x <= len_x - 4:
        if matrix[x][y] == "X" and matrix[x+1][y] == "M" and matrix[x+2][y] == "A" and matrix[x+3][y] == "S":
            count += 1

        if matrix[x][y] == "S" and matrix[x+1][y] == "A" and matrix[x+2][y] == "M" and matrix[x+3][y] == "X":
            count += 1

    if x <= len_x - 4 and y <= len_y - 4:
        if matrix[x][y] == "X" and matrix[x+1][y+1] == "M" and matrix[x+2][y+2] == "A" and matrix[x+3][y+3] == "S":
            count += 1

        if matrix[x][y] == "S" and matrix[x+1][y+1] == "A" and matrix[x+2][y+2] == "M" and matrix[x+3][y+3] == "X":
            count += 1

    if x >= 3 and y <= len_y - 4:
        if matrix[x][y] == "X" and matrix[x-1][y+1] == "M" and matrix[x-2][y+2] == "A" and matrix[x-3][y+3] == "S":
            count += 1

        if matrix[x][y] == "S" and matrix[x-1][y+1] == "A" and matrix[x-2][y+2] == "M" and matrix[x-3][y+3] == "X":
            count += 1

    return count


matrix = get_input()

result = 0

for i, row in enumerate(matrix):
    for j, cell in enumerate(row):
        result += check_field(matrix, i, j)

print(result)
