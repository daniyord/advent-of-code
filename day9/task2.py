from itertools import repeat

with open('input_demo.txt', 'r') as file:
    input = file.readline().strip()

    mode = 'digit'
    file_id = 0

    symbols = []
    for digit in input:
        if mode == 'digit':
            symbols.extend(repeat(str(file_id), int(digit)))
            mode = 'space'
            file_id += 1
            continue
        if mode == 'space':
            symbols.extend(repeat('.', int(digit)))
            mode = 'digit'
            continue

start = 0
end = len(symbols) - 1

print("".join(symbols), len(symbols))

index = 0
while (start < end):
    symbol = None
    symbolCount = 0
    for i in range(end, 0, -1):
        if symbols[i] != '.':
            print("--", symbol)
            if symbol is None:
                symbol = symbols[i]
                symbolCount = 1
                print("alabala", symbol)
            elif symbol != symbols[i]:
                end = i + 1
                break
            else:
                symbolCount += 1

    print(end, symbol, symbolCount)

    exit(1)

    # while
    # for i in range(start, len(symbols) - 1):
    #     if symbols[i] == '.':
    #         start = i
    #         break

    print(start, end)
    # print("".join(symbols))

    if start < end:
        # temp = symbols[start]
        symbols[start] = symbols[end]
        symbols[end] = "."

print("-------------------------------------------")
print("".join(symbols))

result = 0
for index, symbol in enumerate(symbols):
    if symbol == '.':
        break

    result += index * int(symbol)

print(result)
