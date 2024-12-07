from shared import get_input, move
import time


def find_path(matrix, start_x, start_y):
    direction = "up"
    operation = "move"

    visited_places = []

    while (operation != "stop"):
        operation, start_x, start_y = move(direction, matrix, start_x, start_y)

        key = f"{start_x}_{start_y}"

        if operation == "move":
            if not key in visited_places:
                visited_places.append(key)

        if operation in ["up", "right", "down", "left"]:
            direction = operation

    return visited_places


matrix, p_x, p_y = get_input()

start = time.time()

visited_places = find_path(matrix, p_x, p_y)

end = time.time()

print(len(visited_places), (end - start) * 1000)
