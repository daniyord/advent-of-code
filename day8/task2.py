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

            result.add(first)
            result.add(second)

            corection_i1 = -(second[0] - first[0])
            corection_j1 = -(second[1] - first[1])

            i1 = first[0] + corection_i1
            j1 = first[1] + corection_j1

            while 0 <= i1 < len(matrix) and 0 <= j1 < len(matrix[0]):
                result.add((i1, j1))

                if matrix[i1][j1] == ".":
                    matrix[i1][j1] = "#"

                i1 = i1 + corection_i1
                j1 = j1 + corection_j1

            corection_i2 = second[0] - first[0]
            corection_j2 = second[1] - first[1]

            i2 = second[0] + corection_i2
            j2 = second[1] + corection_j2

            while 0 <= i2 < len(matrix) and 0 <= j2 < len(matrix[0]):
                result.add((i2, j2))

                if matrix[i2][j2] == ".":
                    matrix[i2][j2] = "#"

                i2 = i2 + corection_i2
                j2 = j2 + corection_j2

            # print(first, second, "----------------------------------------")
            # for line in matrix:
            #     print(line)

for line in matrix:
    print(line)

print(len(result))
