def construct_dict(list):
    constructed_dict = dict()

    for item in list:
        if item in constructed_dict:
            constructed_dict[item] += 1
        else:
            constructed_dict[item] = 1

    return constructed_dict


left_list = []
right_list = []

with open('input.txt', 'r') as file:
    for line in file:
        line_parts = line.strip().split("   ")

        left_list.append(int(line_parts[0]))
        right_list.append(int(line_parts[1]))

# 0(n*n)
result = 0

for left in left_list:
    count = 0

    for right in right_list:
        if left == right:
            count += 1

    result += (left * count)

print(result)

# 0(n)
result = 0

left_dict = construct_dict(left_list)
right_dict = construct_dict(right_list)

for key in left_dict:
    if key in right_dict:
        result += key * left_dict[key] * right_dict[key]

print(result)
