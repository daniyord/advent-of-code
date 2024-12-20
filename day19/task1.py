from shared import get_input, find_patterns

patterns, designs = get_input("input.txt")
# print(patterns)

result = 0
for design in designs:
    if find_patterns(design, patterns):
        result += 1
    exit(0)

print(result)
