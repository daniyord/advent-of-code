from shared import get_input

matrix, antenas = get_input()

for line in matrix:
    print(line)

for symbol in antenas:
    print(symbol, antenas[symbol])

result = set()

for symbol in antenas:
    symbol_antenas = antenas[symbol]

    for i in range(0, len(symbol_antenas)):
        for j in range(i+1, len(symbol_antenas)):
            first = symbol_antenas[i]
            second = symbol_antenas[j]

            i1 = first[0] - (second[0] - first[0])
            i2 = second[0] + (second[0] - first[0])

            j1 = first[1] - (second[1] - first[1])
            j2 = second[1] + (second[1] - first[1])

            # print(first, second, (i1, j1), (i2, j2))

            if 0 <= i1 < len(matrix) and 0 <= j1 < len(matrix[0]):
                result.add((i1, j1))
                matrix[i1][j1] = "#"

            if 0 <= i2 < len(matrix) and 0 <= j2 < len(matrix[0]):
                result.add((i2, j2))
                matrix[i2][j2] = "#"

            # for line in matrix:
            #     print(line)

            # exit(0)

for line in matrix:
    print(line)

print(len(result))
