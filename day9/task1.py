from shared import get_input

symbols = get_input()

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

    if start < end:
        symbols[start] = symbols[end]
        symbols[end] = "."

# print("".join(symbols))

result = 0
for index, symbol in enumerate(symbols):
    if symbol == '.':
        break

    result += index * int(symbol)

print(result)
