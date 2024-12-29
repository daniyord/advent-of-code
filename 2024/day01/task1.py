left_list = []
right_list = []

with open('input.txt', 'r') as file:
    for line in file:
        line_parts = line.strip().split("   ")

        left_list.append(int(line_parts[0]))
        right_list.append(int(line_parts[1]))


left_list.sort()
right_list.sort()

result = 0

for index, item in enumerate(left_list):
    result += abs(item - right_list[index])

print(result)
