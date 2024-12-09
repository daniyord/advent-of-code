from itertools import repeat

with open('input.txt', 'r') as file:
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

index = 0
while (start < end):
    for i in range(start, len(symbols) - 1):
        if symbols[i] == '.':
            start = i
            break

    for i in range(end, 0, -1):
        if symbols[i] != '.':
            end = i
            break

    print(start, end)
    # print("".join(symbols))

    if start < end:
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
