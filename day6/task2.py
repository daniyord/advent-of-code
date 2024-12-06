from shared import get_input, move
import time

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

start = time.time()

for i, row in enumerate(matrix):
    for j, _ in enumerate(row):
        if matrix[i][j] == ".":
            matrix[i][j] = "#"

            start_process = time.time()
            process_result = process(matrix, p_x, p_y)
            end_process = time.time()

            if process_result == "loop":
                result += 1

            print(process_result, result, index,
                  (end_process - start_process) * 1000)
            index += 1

            matrix[i][j] = "."

end = time.time()

print(result, end - start)
