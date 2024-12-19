from shared import get_input

r_a, r_b, r_c, code = get_input("input.txt")
i_p = 0


def get_literal(code, i_p):
    return code[i_p + 1]


def get_combo(code, i_p, r_a, r_b, r_c):
    match code[i_p + 1]:
        case 0:
            return code[i_p + 1]
        case 1:
            return code[i_p + 1]
        case 2:
            return code[i_p + 1]
        case 3:
            return code[i_p + 1]
        case 4:
            return r_a
        case 5:
            return r_b
        case 6:
            return r_c


def op_jnz(r_a, literal):
    if r_a == 0:
        return i_p + 2
    else:
        return literal


output = []
while (i_p < len(code)):
    instruction = code[i_p]
    literal = get_literal(code, i_p)
    combo = get_combo(code, i_p, r_a, r_b, r_c)

    # print(code, i_p, r_a, r_b, r_c, instruction, literal, combo)
    # print(output)
    # print()
    # input()

    match instruction:
        case 0:  # adv
            r_a = r_a // 2 ** combo
            i_p += 2
        case 1:  # bxl
            r_b = r_b ^ literal
            i_p += 2
        case 2:  # bst
            r_b = combo % 8
            i_p += 2
        case 3:  # jnz
            i_p = op_jnz(r_a, literal)
        case 4:  # bxc
            r_b = r_b ^ r_c
            i_p += 2
        case 5:  # out
            output.append(combo % 8)
            i_p += 2
        case 6:  # bdv
            r_b = r_a // 2 ** combo
            i_p += 2
        case 7:  # cdv
            r_c = r_a // 2 ** combo
            i_p += 2


print(",".join([str(x) for x in output]))
