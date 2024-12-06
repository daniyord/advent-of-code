from shared import get_input, move, find_path
import time

matrix, start_x, start_y = get_input()
visited_places = find_path(matrix, start_x, start_y)

print(len(visited_places))


def check_for_loop(matrix, start_x, start_y):
    direction = "up"
    operation = "move"
    visited_places = []

    while (operation != "stop"):
        operation, start_x, start_y = move(direction, matrix, start_x, start_y)

        if operation in ["up", "right", "down", "left"]:
            direction = operation
            continue

        key = f"{start_x}_{start_y}_{direction}"

        if key in visited_places:
            return "loop"
        else:
            visited_places.append(key)

    return "stop"


result = 0
index = 0

start = time.time()

for key in visited_places:
    index += 1

    if key == f"{start_x}_{start_y}":
        continue

    parts = key.split("_")

    check_x = int(parts[0])
    check_y = int(parts[1])

    start_process = time.time()
    matrix[check_y][check_x] = "#"

    # for line in matrix:
    #     print(line)

    process_result = check_for_loop(matrix, start_x, start_y)
    matrix[check_y][check_x] = "."
    end_process = time.time()

    if process_result == "loop":
        result += 1

    print(index, process_result, result, (end_process - start_process) * 1000)


end = time.time()

print(result, end - start)
