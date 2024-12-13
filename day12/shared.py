import string

def add_place(areas, key, place):
    if not key in areas:
        areas[key] = []

    areas[key].append(place)

def find_connected_places(matrix, areas, i, j, value):
    matrix[i][j] = value 
    add_place(areas, value, (i, j))

    if i > 0 and matrix[i-1][j] == value[0]:
        find_connected_places(matrix, areas, i-1, j, value)        
    if i < len(matrix) - 1 and matrix[i+1][j] == value[0]:
        find_connected_places(matrix, areas, i+1, j, value)
    if j > 0 and matrix[i][j-1] == value[0]:
        find_connected_places(matrix, areas, i, j-1, value)
    if j < len(matrix[0]) - 1 and matrix[i][j+1] == value[0]:
        find_connected_places(matrix, areas, i, j+1, value)

def prepare_input(matrix):
    indexer = {}
    for letter in string.ascii_uppercase:
        indexer[letter] = 0

    areas = {}
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if len(cell) == 1:
                indexer[cell]+= 1
                cell += f"_{indexer[cell]}"
                find_connected_places(matrix, areas, i, j, cell)

    return (matrix, areas)