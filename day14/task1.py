from shared import print_matrix, create_matrix, get_points_and_velocities, process_points


def calculate(filename, max_x, max_y, seconds):
    matrix = create_matrix(max_y, max_x)
    points, velocities = get_points_and_velocities(matrix, filename)

    # print(points)
    # print(velocities)
    # print_matrix(matrix)

    for _ in range(0, seconds):
        process_points(points, velocities, matrix, max_x, max_y)
        # print_matrix(matrix)

    quad1 = 0
    quad2 = 0
    quad3 = 0
    quad4 = 0
    for point in points:
        p_x = point[0]
        p_y = point[1]

        if p_x > max_x // 2 and p_y > max_y // 2:
            quad1 += 1
        if p_x > max_x // 2 and p_y < max_y // 2:
            quad2 += 1
        if p_x < max_x // 2 and p_y > max_y // 2:
            quad3 += 1
        if p_x < max_x // 2 and p_y < max_y // 2:
            quad4 += 1

    # print_matrix(matrix)
    # print(quad1, quad2, quad3, quad4)

    return quad1 * quad2 * quad3 * quad4


print(calculate("input.txt", 101, 103, 100))
# print(calculate("input_demo.txt", 11, 7, 100))
