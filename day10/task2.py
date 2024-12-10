from shared import get_input, find_trailhead_value


matrix, trailheads = get_input()

for trailhead in trailheads:
    find_trailhead_value(trailhead, 0, matrix, trailheads[trailhead])

sum = 0
for key in trailheads:
    sum += len(trailheads[key])
    # print(f"{key} => {trailheads[key]}")

print(sum)
