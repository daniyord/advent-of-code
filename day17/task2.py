from shared import get_input, get_literal, get_combo, op_jnz

r_a, r_b, r_c, code = get_input("input_demo2.txt")
i_p = 0

r_b_org = r_b
r_c_org = r_c

output = []

depth = 1
r_a = depth


def reset_state(depth):
    r_a = depth
    r_b = r_b_org
    r_c = r_c_org

    return (r_a, r_b, r_c, 0, [])


while depth < 150000:
    if i_p >= len(code):
        depth += 1
        r_a, r_b, r_c, i_p, output = reset_state(depth)
        print(f"calculating1: {depth}")
        continue

    instruction = code[i_p]
    literal = get_literal(code, i_p)
    combo = get_combo(code, i_p, r_a, r_b, r_c)

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
            i_p = op_jnz(i_p, r_a, literal)
        case 4:  # bxc
            r_b = r_b ^ r_c
            i_p += 2
        case 5:  # out
            output.append(combo % 8)

            if code[:len(output)] != output or len(output) > len(code):
                depth += 1
                r_a, r_b, r_c, i_p, output = reset_state(depth)
                print(f"calculating2: {depth}")
            elif len(output) == len(code):
                print(f"success: {depth}")
                exit(0)
            else:
                i_p += 2
        case 6:  # bdv
            r_b = r_a // 2 ** combo
            i_p += 2
        case 7:  # cdv
            r_c = r_a // 2 ** combo
            i_p += 2


print("not success")
