from shared import calculate, get_input

input = get_input()

result = 0
start = 0
end = 0

while (True):
    if input[start:].find("don't()") == -1:
        result += calculate(input[start:])
        break
    else:
        end = start + input[start:].find("don't()")
        result += calculate(input[start:end])
        start = end + input[end:].find("do()")


print(result)
