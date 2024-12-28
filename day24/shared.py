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
