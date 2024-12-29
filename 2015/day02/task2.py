import math

file = open("input.txt")

total = 0

for line in file:
    line = line.strip()

    sides = [int(x) for x in line.split("x")]

    present = 2 * min(
        sides[0] + sides[1],
        sides[0] + sides[2],
        sides[1] + sides[2])

    bow = math.prod(sides)

    line_total = present + bow

    total += line_total


print(total)
