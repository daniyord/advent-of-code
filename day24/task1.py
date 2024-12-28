from shared import get_input

(wires, gates) = get_input('input.txt')

# print(wires)
# print(gates)

while len(gates) > 0:
    for gate in gates:
        is_processed = False
        if gate[1] in wires and gate[2] in wires:
            is_processed = True
            match gate[0]:
                case "AND":
                    wires[gate[3]] = wires[gate[1]] & wires[gate[2]]
                case "OR":
                    wires[gate[3]] = wires[gate[1]] | wires[gate[2]]
                case "XOR":
                    check = wires[gate[1]] != wires[gate[2]]
                    wires[gate[3]] = 1 if check else 0

        if is_processed:
            gates.remove(gate)
            continue

# print(wires)

result = 0
degree = 0

for wire in sorted(wires):
    if wire.startswith("z"):
        if wires[wire] > 0:
            result += (2 ** degree) * wires[wire]

        degree += 1

print(result)
