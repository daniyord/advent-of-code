def print_matrix(matrix):
    print()
    for line in matrix:
        print("".join([str(x) for x in line]))


def create_matrix(h, v):
    matrix = []

    for i in range(0, h):
        matrix.append([])
        for j in range(0, v):
            matrix[i].append(0)

    return matrix


def get_points_and_velocities(matrix, filename):
    points = []
    velocities = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(" ")

            point = parts[0].replace("p=", "").split(",")
            velocity = parts[1].replace("v=", "").split(",")

            p_x = int(point[0])
            p_y = int(point[1])

            matrix[p_y][p_x] += 1

            points.append((p_x, p_y))
            velocities.append((int(velocity[0]), int(velocity[1])))

    return (points, velocities)


def process_points(points, velocities, matrix, max_x, max_y):
    for i, point in enumerate(points):
        p_x = point[0]
        p_y = point[1]

        matrix[p_y][p_x] -= 1

        velocity = velocities[i]
        v_x = velocity[0]
        v_y = velocity[1]

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

        matrix[p_y][p_x] += 1
        points[i] = (p_x, p_y)
