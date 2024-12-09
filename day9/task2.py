from shared import get_input

symbols = get_input()

start = 0
end = len(symbols) - 1

print("".join(symbols), len(symbols))

while (start < end):
    symbol = None
    symbol_count = 0
    for i in range(end, 0, -1):
        if symbol is not None and symbol != symbols[i]:
            end = i + 1
            break

        if symbols[i] != '.':
            if symbol is None:
                symbol = symbols[i]
                symbol_count = 1
            else:
                symbol_count += 1

    empty_count = 0
    empty_start = None
    first_empty_passed = False
    for i in range(start, end):
        if symbols[i] == '.':
            if not first_empty_passed:
                start = i
                first_empty_passed = True

            if empty_start is None:
                empty_start = i
                empty_count = 1
            else:
                empty_count += 1
        else:
            if empty_start is not None:
                if empty_count >= symbol_count:
                    break
                else:
                    empty_count = 0
                    empty_start = None

    if symbol_count > 0 and empty_count > 0 and empty_count >= symbol_count:
        for i in range(0, symbol_count):
            symbols[empty_start + i] = symbol
            symbols[end + i] = "."

    end -= 1

    print(start, end)


# print("".join(symbols))

result = 0
for index, symbol in enumerate(symbols):
    if symbol != '.':
        result += index * int(symbol)


print(result)
