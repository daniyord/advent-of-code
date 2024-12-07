from shared import get_input, move
import time


def find_path(matrix, start_x, start_y):
    direction = "up"
    operation = "move"

    visited_places = []

    while (operation != "stop"):
        operation, start_x, start_y = move(direction, matrix, start_x, start_y)

        if operation in ["up", "right", "down", "left"]:
            direction = operation
            visited_places[-1] = f"{start_x}_{start_y}_{direction}"
        else:
            visited_places.append(f"{start_x}_{start_y}_{direction}")

    return visited_places


def check_for_loop(direction, matrix, start_x, start_y, must_print):
    if must_print:
        for line in matrix:
            print(line)

    operation = "move"
    visited_places = set()

    while (operation != "stop"):
        if must_print:
            print(start_x, start_y, direction)

        operation, start_x, start_y = move(direction, matrix, start_x, start_y)

        if operation in ["up", "right", "down", "left"]:
            direction = operation
            continue

        key = f"{start_x}_{start_y}_{direction}"

        if key in visited_places:
            return "loop"
        else:
            visited_places.add(key)

    return "stop"


matrix, start_x, start_y = get_input()
visited_places = find_path(matrix, start_x, start_y)

result = set()
start = time.time()

for index in range(1, len(visited_places) - 1):
    current = visited_places[index]
    next = visited_places[index+1]

    if current == f"{start_x}_{start_y}":
        continue

    next_parts = next.split("_")

    next_x = int(next_parts[0])
    next_y = int(next_parts[1])

    start_process = time.time()

    matrix[next_y][next_x] = "#"

    must_print = False
    # if next == "6_7_right":
    #     must_print = True

    process_result = check_for_loop("up", matrix, start_x, start_y, must_print)

    matrix[next_y][next_x] = "."

    end_process = time.time()

    if process_result == "loop":
        result.add(f"{next_x}_{next_y}")

    print(next, process_result, len(result),
          (end_process - start_process) * 1000)

end = time.time()

print(len(result), end - start)
