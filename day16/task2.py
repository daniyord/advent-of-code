import sys
sys.path.append('..')

from utils import print_matrix_compact, print_dict
from shared import get_input, shortest_path

marked = set()


def process(f, visited, matrix):
    # print(f)
    marked.add((f[0], f[1]))
    matrix[f[1]][f[0]] = "0"

    if visited[f][1] is not None:
        for l in visited[f][1]:
            process(l, visited, matrix)


matrix, start = get_input("input_demo1.txt")

print(f"start: {start}")
print_matrix_compact(matrix)

found_min, found, visited = shortest_path(matrix, start)

# print(found)


for f in found:
    process(f, visited, matrix)

print()
print_matrix_compact(matrix)

# print(marked)
print(len(marked))
# print(found)
# print(found_min)
