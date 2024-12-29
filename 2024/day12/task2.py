import sys
sys.path.append('..')

from utils import print_matrix, print_dict, read_matrix
from shared import prepare_input


def modify_num_sides(sides, type, value, start, end):
    key = f"{type}_{value}"

    if key not in sides:
        sides[key] = []

    sides[key].append((start, end))
    sides[key].sort()

    # print(f"modify_num_sides: {type} {value} {start} {end}")


def calculate_num_sides(area):
    sides = {}

    for place in area:
        if (place[0] - 1, place[1]) not in area:
            modify_num_sides(sides, "ht", place[0], place[1], place[1] + 1)
        if (place[0], place[1] - 1) not in area:
            modify_num_sides(sides, "vl", place[1], place[0], place[0] + 1)
        if (place[0] + 1, place[1]) not in area:
            modify_num_sides(sides, "hb", place[0] + 1, place[1], place[1] + 1)
        if (place[0], place[1] + 1) not in area:
            modify_num_sides(sides, "vr", place[1] + 1, place[0], place[0] + 1)

    print_dict(sides)

    num_sides = 0
    for key in sides:
        side = sides[key]

        count = 1
        for i in range(0, len(side) - 1):
            current = side[i]
            next = side[i + 1]

            if current[1] != next[0]:
                count += 1

        num_sides += count
        # print(side)

    return num_sides

# ------------------------------------------------------------------------------------


matrix = read_matrix('input.txt')

print_matrix(matrix)

matrix, areas = prepare_input(matrix)

print()
print_matrix(matrix)
print()
print_dict(areas)
print()

result = 0
for area_key in areas:
    num_sides = calculate_num_sides(areas[area_key])
    rank = len(areas[area_key])

    result += num_sides * rank

    print(area_key, num_sides, rank, num_sides * rank, result)
    print()


print(result)
