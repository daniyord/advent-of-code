
left_list = []
right_list = []

with open('input.txt', 'r') as file:
    for line in file:
        line_parts = line.strip().split("   ")

        left_list.append(int(line_parts[0]))
        right_list.append(int(line_parts[1]))

result = 0

for left in left_list:
    count = 0

    for right in right_list:
        if left == right:
            count += 1

    result += (left * count)

print(result)
