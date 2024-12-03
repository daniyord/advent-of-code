import re


def get_input():
    with open("input.txt", 'r') as file:
        input = file.read()
    return input


def calculate(input):
    matches = re.findall(r"mul\([0-9]*,[0-9]*\)", input)

    result = 0

    for match in matches:
        parts = match.replace("mul(", "").replace(")", "").split(",")

        result += (int)(parts[0]) * (int)(parts[1])

    return result
