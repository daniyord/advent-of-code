from shared import get_input, find_patterns

patterns, designs = get_input("input.txt")

result = 0
for design in designs:
    result += find_patterns(design, patterns)

print(result)
