result = 0


def is_save_report(line_parts):
    if line_parts[0] > line_parts[1]:
        check_desc = True
    elif line_parts[0] < line_parts[1]:
        check_desc = False
    else:
        return False

    is_save = True
    for index, current in enumerate(line_parts):
        prev = line_parts[index-1]

        if index == 0:
            continue

        if current == prev:
            is_save = False
            continue

        if abs(current - prev) > 3:
            is_save = False
            continue

        if check_desc and current > prev:
            is_save = False
            continue

        if not check_desc and current < prev:
            is_save = False
            continue

    return is_save


with open('input.txt', 'r') as file:
    for line in file:
        line_parts = [int(x) for x in line.strip().split(" ")]

        is_save = False

        for index, current in enumerate(line_parts):
            new_check = line_parts[0:index] + line_parts[index+1:]

            is_save = is_save or is_save_report(new_check)

        print(line_parts, is_save)

        if is_save:
            result += 1


print(result)
