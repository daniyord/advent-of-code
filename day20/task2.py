import sys
sys.path.append('..')

from utils import read_matrix, print_matrix_compact, print_matrix, print_dict
from shared import find_short_path, restore_path


matrix, start, end = read_matrix("input.txt")

founded, visited = find_short_path(matrix, start, end)

founded_path = restore_path(visited, founded) + [start]

founded_path = list(reversed(founded_path))

# print(len(founded_path))
# print(founded_path)

border = 0
total = len(founded_path)

result = 0
result_dict = {}
total = len(founded_path)

for i in range(0, len(founded_path)):
    for j in range(i + 1, len(founded_path)):
        first = founded_path[i]
        second = founded_path[j]

        first_to_end = total - i
        second_to_end = total - j
        first_to_second = first_to_end - second_to_end
        manhatan = abs(first[0] - second[0]) + abs(first[1] - second[1])

        if manhatan <= 20:
            diff = first_to_second - manhatan
            if diff >= 50:
                if diff not in result_dict:
                    result_dict[diff] = 0
                result_dict[diff] += 1

                result += 1

print_dict(result_dict)
print(result)

# 32 + 31 + 29 + 39 + 25 + 23 + 20 + 19 + 12 + 14 + 12 + 22 + 4 + 3 = 285

# There are 32 cheats that save 50 picoseconds.
# There are 31 cheats that save 52 picoseconds.
# There are 29 cheats that save 54 picoseconds.
# There are 39 cheats that save 56 picoseconds.
# There are 25 cheats that save 58 picoseconds.
# There are 23 cheats that save 60 picoseconds.
# There are 20 cheats that save 62 picoseconds.
# There are 19 cheats that save 64 picoseconds.
# There are 12 cheats that save 66 picoseconds.
# There are 14 cheats that save 68 picoseconds.
# There are 12 cheats that save 70 picoseconds.
# There are 22 cheats that save 72 picoseconds.
# There are 4 cheats that save 74 picoseconds.
# There are 3 cheats that save 76 picoseconds.

# 1010263
# 245213

1240174
