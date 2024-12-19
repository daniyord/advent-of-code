import sys
sys.path.append('..')

from utils import print_matrix_compact
from shared import get_input, short_path


# matrix, next_falling = get_input("input_demo.txt", 7, 12)
matrix, next_falling = get_input("input.txt", 71, 1024)


# print_matrix_compact(matrix)

for next in next_falling:
    # print(next)

    x = next[0]
    y = next[1]

    matrix[y][x] = "#"

    # found_min = short_path(matrix, (6, 6))
    found_min = short_path(matrix, (70, 70))

    if found_min is None:
        print(next)
        exit(0)
