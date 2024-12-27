import networkx as nx
from shared import get_commands, numeric_keypad_graph, directional_keypad_graph
from itertools import permutations

cache = {}


def get_replacement(directional_keypad_graph, start, end):
    key = f"{start}{end}"

    if key in cache:
        return cache[key]

    codes = get_commands(f"{start}{end}", directional_keypad_graph())

    # print("codes:", codes)

    tmp = []
    for code in codes:
        sub_codes = get_commands(code, directional_keypad_graph())
        # print("sub_codes:", sub_codes)
        tmp.append(len(sub_codes[0]))

    print(key, tmp)

    # if len(codes) == 1:
    #     cache[key] = codes[0]
    #     return codes[0]

    # min_codes = None
    # for code in codes:
    #     sub_codes = get_commands(code, directional_keypad_graph)
    #     if min_codes is None or len(min_codes) >


# for (first, second) in permutations("<>^vA", 2):
#     get_replacement(directional_keypad_graph, first, second)

# get_replacement(directional_keypad_graph, "A", "<")

codes_2 = get_commands('A<', directional_keypad_graph())
print(codes_2)

# codes_3 = get_commands('<^A>A', directional_keypad_graph())
# print(codes_3)

# <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
# v<<A>>^A<A>AvA<^AA>A<vAAA>^A
# <A^A>^^AvvvA
# 029A


#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

# A < A
# A ^ A
# A > ^ ^ A
# AvvvA
