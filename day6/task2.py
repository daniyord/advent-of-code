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
        else:
            visited_places.append(f"{start_x}_{start_y}")

    return visited_places


def check_for_loop(direction, matrix, start_x, start_y):
    operation = "move"
    visited_places = []

    while (operation != "stop"):
        # print("---", direction,  start_x, start_y)

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


matrix, start_x, start_y = get_input()
visited_places = find_path(matrix, start_x, start_y)

# print(visited_places)
# exit(0)

# for line in matrix:
#     print(line)
# print()

result = 0
start = time.time()

for index, key in enumerate(visited_places):
    if index == len(visited_places) - 1:
        break

    check_next = False

    # if key == f"{start_x}_{start_y}":
    #     continue

    parts = key.split("_")

    check_x = int(parts[0])
    check_y = int(parts[1])

    next_parts = visited_places[index+1].split("_")

    next_x = int(next_parts[0])
    next_y = int(next_parts[1])

    if check_x == next_x and check_y == next_y:
        continue

    if check_y > next_y:
        direction = "right"

    if check_x < next_x:
        direction = "down"

    if check_y < next_y:
        direction = "left"

    if check_x > next_x:
        direction = "up"

    start_process = time.time()

    matrix[next_y][next_x] = "#"

    # for line in matrix:
    #     print(line)

    if check_x == 3 and check_y == 6 and next_x == 2 and next_y == 6:
        print(direction, check_x, check_y, next_x, next_y)
        print(matrix[next_x][next_y])
        for line in matrix:
            print(line)
        print()

    # print("----", direction, check_x, check_y, next_x, next_y)

    process_result = check_for_loop(direction, matrix, check_x, check_y)

    matrix[next_y][next_x] = "."
    end_process = time.time()

    if process_result == "loop":
        # print("-----------", direction, check_x, check_y, next_x, next_y)
        result += 1

    print(process_result, result, (end_process - start_process) * 1000)


end = time.time()

print(result, end - start)
