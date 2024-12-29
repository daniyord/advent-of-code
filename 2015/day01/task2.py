file = open("input.txt")

content = file.read()

result = 0
for index, symbol in enumerate(content):
    if symbol == "(":
        result += 1
    if symbol == ")":
        result -= 1

    if result == -1:
        print(index + 1)
        break
