import sys
sys.path.append('..')

from utils import print_matrix, print_dict, read_matrix
# from shared import prepare_input


def print_matrix_1(matrix):
    for line in matrix:
        print("".join(line))


def create_matrix(h, v):
    matrix = []

    for i in range(0, h):
        matrix.append([])
        for j in range(0, v):
            if j != v // 2 and i != h // 2:
                matrix[i].append(".")
            else:
                matrix[i].append(" ")

    return matrix


def get_points_and_velocities(filename):
    points = []
    velocities = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(" ")

            point = parts[0].replace("p=", "").split(",")
            velocity = parts[1].replace("v=", "").split(",")

            points.append((int(point[0]), int(point[1])))
            velocities.append((int(velocity[0]), int(velocity[1])))

    return (points, velocities)


max_x = 101
max_y = 103
seconds = 100

points, velocities = get_points_and_velocities('input.txt')
matrix = create_matrix(max_y, max_x)

# print(points)
# print(velocities)
# print_matrix(matrix)

quad1 = 0
quad2 = 0
quad3 = 0
quad4 = 0

for i, point in enumerate(points):
    p_x = point[0]
    p_y = point[1]

    velocity = velocities[i]
    v_x = velocity[0]
    v_y = velocity[1]

    # print(p_x, p_y)

    for i in range(0, seconds):
        p_x += v_x
        p_y += v_y

        if p_x < 0:
            p_x = max_x + p_x

        if p_x >= max_x:
            p_x = p_x - max_x

        if p_y < 0:
            p_y = max_y + p_y

        if p_y >= max_y:
            p_y = p_y - max_y

        # print(f"{i}: ({p_x}, {p_y})")

    if p_x > max_x // 2 and p_y > max_y // 2:
        quad1 += 1
    if p_x > max_x // 2 and p_y < max_y // 2:
        quad2 += 1
    if p_x < max_x // 2 and p_y > max_y // 2:
        quad3 += 1
    if p_x < max_x // 2 and p_y < max_y // 2:
        quad4 += 1

    if matrix[p_y][p_x] == " ":
        continue

    if matrix[p_y][p_x] == ".":
        matrix[p_y][p_x] = "1"
    else:
        matrix[p_y][p_x] = str(int(matrix[p_y][p_x]) + 1)

# print_matrix_1(matrix)
# print(quad1, quad2, quad3, quad4)

print(quad1 * quad2 * quad3 * quad4)
