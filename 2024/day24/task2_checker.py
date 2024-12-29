from shared import get_input, process

(wires, gates) = get_input('input_fixed.txt')
process(wires, gates)

result_x = 0
degree_x = 0

result_y = 0
degree_y = 0

result_z = 0
degree_z = 0

for wire in sorted(wires):
    if wire.startswith("x"):
        if wires[wire] > 0:
            result_x += (2 ** degree_x) * wires[wire]

        degree_x += 1

    if wire.startswith("y"):
        if wires[wire] > 0:
            result_y += (2 ** degree_y) * wires[wire]

        degree_y += 1

    if wire.startswith("z"):
        if wires[wire] > 0:
            result_z += (2 ** degree_z) * wires[wire]

        degree_z += 1

print(result_x, result_y, result_z)

print(result_x + result_y == result_z)
