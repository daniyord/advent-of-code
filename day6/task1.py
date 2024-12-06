from shared import get_input, move


matrix, p_x, p_y = get_input()
direction = "up"
operation = "move"

found_places = []

while (operation != "stop"):
    operation, p_x, p_y = move(direction, matrix, p_x, p_y)

    if operation == "move":
        if not f"{p_x}_{p_y}" in found_places:
            found_places.append(f"{p_x}_{p_y}")

    elif operation != "stop":
        direction = operation

    # print(p_x, p_y, operation)

print(len(found_places))
