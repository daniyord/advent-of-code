import sys
sys.path.append('..')

from utils import print_matrix_compact, print_dict
from shared import get_input, shortest_path
import time

start_time = time.time()


marked = set()


def process(f, visited, matrix):
    # print(f)
    marked.add((f[0], f[1]))
    matrix[f[1]][f[0]] = "0"

    if visited[f][1] is not None:
        for l in visited[f][1]:
            process(l, visited, matrix)


matrix, start = get_input("input.txt")

print(f"start: {start}")
print_matrix_compact(matrix)

found_min, found, visited = shortest_path(matrix, start)

# print(found)


for f in found:
    process(f, visited, matrix)

print()
print_matrix_compact(matrix)

# print(marked)
# print(len(marked))
# print(found)
# print(found_min)

end_time = time.time()

print(f"task2: {len(marked)}", f"{(end_time - start_time) * 1000}ms")
