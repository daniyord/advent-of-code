import sys
sys.path.append('..')

from utils import print_matrix_compact
from shared import get_input, short_path


# matrix = get_input("input_demo.txt", 7, 12)
# found_min, _, _ = short_path(matrix, (6, 6))

matrix, _ = get_input("input.txt", 71, 1024)
found_min = short_path(matrix, (70, 70))

# print_matrix_compact(matrix)

print(found_min)
