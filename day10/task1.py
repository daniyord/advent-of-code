from shared import get_input, print_matrix


def find_trailhead_value(trailhead, current, matrix, founds):
    if current == 9:
        founds.add(trailhead)

    i = trailhead[0]
    j = trailhead[1]

    if i >= 1 and matrix[i-1][j] == current+1:
        find_trailhead_value((i-1, j), current+1, matrix, founds)

    if i <= len(matrix)-2 and matrix[i+1][j] == current+1:
        find_trailhead_value((i+1, j), current+1, matrix, founds)

    if j >= 1 and matrix[i][j-1] == current+1:
        find_trailhead_value((i, j-1), current+1, matrix, founds)

    if j <= len(matrix[0])-2 and matrix[i][j+1] == current+1:
        find_trailhead_value((i, j+1), current+1, matrix, founds)


matrix, trailheads = get_input()

# print(trailheads)
# print_matrix(matrix)

for trailhead in trailheads:
    find_trailhead_value(trailhead, 0, matrix, trailheads[trailhead])

sum = 0
for key in trailheads:
    sum += len(trailheads[key])
    # print(f"{key} => {trailheads[key]}")

print(sum)
