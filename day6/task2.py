from shared import get_input, move


matrix, p_x, p_y = get_input()

print(len(matrix) * len(matrix[0]))


def process(matrix, p_x, p_y):
    direction = "up"

    operation = "move"

    visited_places = []

    while (operation != "stop"):
        operation, p_x, p_y = move(direction, matrix, p_x, p_y)

        if operation in ["up", "right", "down", "left"]:
            direction = operation
            continue

        key = f"{p_x}_{p_y}_{direction}"

        if key in visited_places:

            return "loop"
        else:
            visited_places.append(key)

    return "stop"


result = 0

index = 0
for i, row in enumerate(matrix):
    for j, _ in enumerate(row):
        if matrix[i][j] == ".":
            matrix[i][j] = "#"

            process_result = process(matrix, p_x, p_y)
            if process_result == "loop":
                result += 1

            print(process_result, result, index)
            index += 1

            matrix[i][j] = "."

print(result)
