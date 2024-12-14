from shared import print_matrix, create_matrix, get_points_and_velocities, process_points


def check_matrix_is_symetric(matrix):
    for row in matrix:
        for cell in row:
            if (cell > 1):
                return False
    return True


def calculate(filename, max_x, max_y):
    matrix = create_matrix(max_y, max_x)
    points, velocities = get_points_and_velocities(matrix, filename)

    index = 0
    while True:
        index += 1

        process_points(points, velocities, matrix, max_x, max_y)

        if check_matrix_is_symetric(matrix):

            print_matrix(matrix)
            print(index)
            break


calculate("input.txt", 101, 103)
