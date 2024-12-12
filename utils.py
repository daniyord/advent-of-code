def read_matrix(filepath):
    with open(filepath, 'r') as file:
        matrix = []
        
        for line in file:
            row = []
            matrix.append(row)

            for symbol in line.strip():
                row.append(symbol)
    
    return matrix

def print_matrix(matrix):
    for line in matrix:
        print(line)

def print_dict(dict):
    for key in dict:
        print(f"{key}: {dict[key]}")
