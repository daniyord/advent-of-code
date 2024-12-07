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


def check_for_loop(direction, matrix, start_x, start_y):
    operation = "move"
    visited_places = []

    while (operation != "stop"):
        # prev_operation = operation

        operation, start_x, start_y = move(direction, matrix, start_x, start_y)

        if operation in ["up", "right", "down", "left"]:
            # if prev_operation == "move":
            #     return "block"

            direction = operation
            continue

        key = f"{start_x}_{start_y}_{direction}"

        if key in visited_places:
            return "loop"
        else:
            visited_places.append(key)

    return "stop"


matrix, start_x, start_y = get_input()
visited_places = find_path(matrix, start_x, start_y)

result = []
start = time.time()

for index in range(1, len(visited_places) - 1):
    current = visited_places[index]
    prev = visited_places[index-1]
    next = visited_places[index+1]

    if current == f"{start_x}_{start_y}":
        continue

    # prev_parts = prev.split("_")

    # prev_x = int(prev_parts[0])
    # prev_y = int(prev_parts[1])
    # prev_direction = prev_parts[2]

    next_parts = next.split("_")

    next_x = int(next_parts[0])
    next_y = int(next_parts[1])

    start_process = time.time()

    matrix[next_y][next_x] = "#"

    process_result = check_for_loop("up", matrix, start_x, start_y)

    matrix[next_y][next_x] = "."

    end_process = time.time()

    if process_result == "loop":
        result.append(f"{next_x}_{next_y}")

    print(process_result, len(result), (end_process - start_process) * 1000)


end = time.time()

print(len(set(result)), end - start)

# ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.']
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#']
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
# ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.']
# ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.']
# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
# ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.']
# ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.']
# ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.']
# ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']
