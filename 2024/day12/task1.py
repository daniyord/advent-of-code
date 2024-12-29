import sys
sys.path.append('..')

from utils import print_matrix, print_dict, read_matrix
from shared import prepare_input


def calculate_parameter1(area):
    result = 0

    for place in area:
        place_perimeter = 4

        if (place[0] - 1, place[1]) in area:
            place_perimeter -= 1
        if (place[0], place[1] - 1) in area:
            place_perimeter -= 1
        if (place[0] + 1, place[1]) in area:
            place_perimeter -= 1
        if (place[0], place[1] + 1) in area:
            place_perimeter -= 1

        result += place_perimeter

    return result


def calculate_parameter(area):
    adj = 0
    for a_i in range(0, len(area)):
        for a_j in range(a_i + 1, len(area)):
            if area[a_i][0] == area[a_j][0] and abs(area[a_i][1] - area[a_j][1]) == 1:
                adj += 1
            if area[a_i][1] == area[a_j][1] and abs(area[a_i][0] - area[a_j][0]) == 1:
                adj += 1

    return 4 * len(area) - 2 * adj

# ------------------------------------------------------------------------------------


matrix = read_matrix('input_demo.txt')

print_matrix(matrix)

matrix, areas = prepare_input(matrix)

print()
print_matrix(matrix)
print_dict(areas)

result = 0
for area_key in areas:
    perimeter = calculate_parameter(areas[area_key])
    rank = len(areas[area_key])

    result += perimeter * rank

    print(area_key, perimeter, rank, perimeter * rank, result)

print(result)
