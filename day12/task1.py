import string


def print_matrix(matrix):
    for line in matrix:
        print(line)


def add_place(dict, key, place):
    if not key in dict:
        dict[key] = []

    dict[key].append(place)


with open('input_demo2.txt', 'r') as file:
    matrix = []
    areas = {}
    indexer = {}

    for letter in string.ascii_uppercase:
        indexer[letter] = 0

    for m_i, line in enumerate(file):
        row = []
        matrix.append(row)

        for m_j, letter in enumerate(line.strip()):
            if m_i > 0 and matrix[m_i-1][m_j][0] == letter:
                row.append(matrix[m_i-1][m_j])
            else:
                row.append(letter)

        for r_i in range(0, len(row)):
            if len(row[r_i]) == 1:
                if r_i > 0 and len(row[r_i-1]) > 1 and row[r_i-1][0] == row[r_i]:
                    row[r_i] = row[r_i-1]

                for r_j in range(r_i+1, len(row)):
                    if row[r_j][0] == row[r_i]:
                        if len(row[r_j]) > 1:
                            row[r_i] = row[r_j]
                            break
                    else:
                        break

                if len(row[r_i]) == 1:
                    indexer[row[r_i]] += 1
                    row[r_i] += f"_{indexer[row[r_i]]}"
            add_place(areas, row[r_i], (m_i, r_i))

# print_matrix(matrix)

result = 0
for area_key in areas:
    area = areas[area_key]
    # print(f"{area_key}: {area}")

    adj = 0
    for a_i in range(0, len(area)):
        for a_j in range(a_i+1, len(area)):
            if area[a_i][0] == area[a_j][0] and abs(area[a_i][1] - area[a_j][1]) == 1:
                adj += 1
            if area[a_i][1] == area[a_j][1] and abs(area[a_i][0] - area[a_j][0]) == 1:
                adj += 1

    result += (4 * len(area) - 2 * adj) * len(area)

    print(f"{area_key}: {area} : {
          (4 * len(area) - 2 * adj) * len(area)}", result)

    input()

print(result)
