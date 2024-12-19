from shared import get_input, shortest_path

matrix, start = get_input("input_demo1.txt")
found_min, _, _ = shortest_path(matrix, start)

print(found_min)
