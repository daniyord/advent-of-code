file = open("input.txt")

total = 0

for line in file:
    line = line.strip()

    sides = [int(x) for x in line.split("x")]

    area1 = sides[0] * sides[1]
    area2 = sides[0] * sides[2]
    area3 = sides[1] * sides[2]

    areas = [area1, area2, area3]

    line_total = 2 * (sum(areas)) + min(areas)

    total += line_total

print(total)
