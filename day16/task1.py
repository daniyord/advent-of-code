from shared import get_input, shortest_path
import time

start_time = time.time()

matrix, start = get_input("input.txt")
found_min, _, _ = shortest_path(matrix, start)

end_time = time.time()

print(f"task1: {found_min}", f"{(end_time - start_time) * 1000}ms")
