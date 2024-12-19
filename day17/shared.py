def get_input(filename):
    file = open(filename, 'r')
    for index, line in enumerate(file):
        line = line.strip()

        match index:
            case 0:
                r_a = int(line.split(":")[1].strip())
            case 1:
                r_b = int(line.split(":")[1].strip())
            case 2:
                r_c = int(line.split(":")[1].strip())
            case 4:
                code = [int(x.strip()) for x in line.split(":")[1].split(",")]

    return (r_a, r_b, r_c, code)


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


def op_jnz(i_p, r_a, literal):
    if r_a == 0:
        return i_p + 2
    else:
        return literal
