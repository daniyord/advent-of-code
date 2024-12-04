from shared import get_input


def check_field(matrix, x, y):
    len_x = len(matrix)
    len_y = len(matrix[0])

    check_left = False
    check_right = False

    if x >= 1 and x <= len_x - 2 and y >= 1 and y <= len_y - 2 and matrix[x][y] == "A":
        if matrix[x-1][y-1] == "M" and matrix[x+1][y+1] == "S":
            check_left = True
        if matrix[x-1][y-1] == "S" and matrix[x+1][y+1] == "M":
            check_left = True

        if matrix[x-1][y+1] == "M" and matrix[x+1][y-1] == "S":
            check_right = True
        if matrix[x-1][y+1] == "S" and matrix[x+1][y-1] == "M":
            check_right = True

    return 1 if check_left and check_right else 0


matrix = get_input()

result = 0

for i, row in enumerate(matrix):
    for j, cell in enumerate(row):
        result += check_field(matrix, i, j)

print(result)
