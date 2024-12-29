import bitarray as ba
import bitarray.util as bau
import itertools as it

from shared import calculate, get_input


def process(filename, start, end, step):
    _, r_b, r_c, code = get_input(filename)
    valid = [ba.bitarray()]

    similarity_num = 0
    is_first = True
    for j in range(start, end + 1, step):
        similarity_num += 1

        if j >= end:
            similarity_num = len(code)

        new_valid = []

        if is_first:
            gen_step = start
            is_first = False
        else:
            gen_step = step

        for v in valid:
            for p in it.product("01", repeat=gen_step):
                b = ba.bitarray("".join(p)) + v

                output = calculate(bau.ba2int(b), r_b, r_c, code)

                if code[:similarity_num] == output[:similarity_num]:
                    new_valid.append(b)

        valid = new_valid

        print(j, similarity_num, len(valid))

    print(bau.ba2int(valid[0]))


# process("input_demo2.txt", 6, 18, 3)
process("input.txt", 12, 48, 3)
