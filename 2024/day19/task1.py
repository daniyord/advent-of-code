from shared import get_input, find_patterns

patterns, designs = get_input("input.txt")

result = 0
for design in designs:
    if find_patterns(design, patterns) > 0:
        result += 1

print(result)
