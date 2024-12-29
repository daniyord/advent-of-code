file = open("input.txt")

keys = []
locks = []

is_key = None
pattern = None

for l_index, line in enumerate(file):
    line = line.strip()
    l_index = l_index % 8

    # print(l_index, line)

    if l_index == 0:
        pattern = [0, 0, 0, 0, 0]
        is_key = line[0] == "#"
        continue

    if 1 <= l_index <= 5:
        for s_i, symbol in enumerate(line):
            if line[s_i] == "#":
                pattern[s_i] += 1

    if l_index == 6:
        if is_key:
            keys.append(pattern)
        else:
            locks.append(pattern)
        continue

print(keys)
print()
print(locks)

result = 0
for key in keys:
    for lock in locks:
        is_valid = True
        for i in range(0, 5):
            if key[i] + lock[i] > 5:
                is_valid = False
                break

        print(key, lock, is_valid)

        if is_valid:
            result += 1

print(result)
