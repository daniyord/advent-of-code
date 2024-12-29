file = open("input.txt")

content = file.read()

result = 0
for symbol in content:
    if symbol == "(":
        result += 1
    if symbol == ")":
        result -= 1

print(result)
