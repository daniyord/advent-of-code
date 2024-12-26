import networkx as nx
from shared import get_commands, numeric_keyboard_graph, command_keyboard_graph


def get_complexity(code):
    codes_1 = get_commands("A" + code, numeric_keyboard_graph())

    min_complexity = None
    for code_1 in codes_1:
        # print("code_1:", code_1)

        codes_2 = get_commands("A" + code_1, command_keyboard_graph())
        for code_2 in codes_2:
            # print("code_2:", code_2)

            codes_3 = get_commands("A" + code_2, command_keyboard_graph())

            for code_3 in codes_3:
                # print("code_3:", code_3)

                if min_complexity is None or min_complexity > len(code_3):
                    min_complexity = len(code_3)

    return min_complexity * int(code.replace("A", "").lstrip("0"))


result = 0
file = open('input.txt', 'r')
for line in file:
    result += get_complexity(line.strip())

print(result)
