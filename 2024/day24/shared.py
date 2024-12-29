def get_input(filename):
    read_gates = False

    wires = {}
    gates = []

    file = open(filename, "r")
    for line in file:
        line = line.strip()

        if len(line) == 0:
            read_gates = True
            continue

        if not read_gates:
            parts = line.split(": ")

            wires[parts[0]] = int(parts[1])
        else:
            parts = line.split(" ")

            gates.append((parts[1], parts[0], parts[2], parts[4]))

    return (wires, gates)


def process(wires, gates):
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
