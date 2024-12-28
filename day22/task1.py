from shared import calculate_next


def calculate_nth(secret, depth):
    for _ in range(0, depth):
        secret = calculate_next(secret)

    return secret


result = 0
file = open('input.txt', 'r')
for line in file:
    result += calculate_nth(int(line.strip()), 2000)

print(result)
