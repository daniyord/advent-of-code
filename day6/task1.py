from shared import get_input, move, find_path


matrix, p_x, p_y = get_input()

visited_places = find_path(matrix, p_x, p_y)
print(len(visited_places))
