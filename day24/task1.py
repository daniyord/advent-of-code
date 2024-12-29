from shared import get_input, process

(wires, gates) = get_input('input.txt')

# print(wires)
# print(gates)

process(wires, gates)

# print(wires)

result = 0
degree = 0

for wire in sorted(wires):
    if wire.startswith("z"):
        if wires[wire] > 0:
            result += (2 ** degree) * wires[wire]

        degree += 1

print(result)
