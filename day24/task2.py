read_gates = False

gates = {}
swaps = []


def find_gate_operator(operation, operator, output):
    for gate in gates:
        if operation == gate[0] and operator in gate[1] and gates[gate] == output:
            return gate[1][0] if gate[1][0] != operator else gate[1][1]


def find_gate_output(operation, pair):
    for gate in gates:
        if operation == gate[0] and pair[0] in gate[1] and pair[1] in gate[1]:
            return gates[gate]


def find_gate_by_output(output):
    for gate in gates:
        if output == gates[gate]:
            return gate


def swap(output1, output2):
    swaps.append(output1)
    swaps.append(output2)

    found1 = find_gate_by_output(output1)
    found2 = find_gate_by_output(output2)

    gates[found1] = output2
    gates[found2] = output1


def print_gate(operation, operators, output):
    print(f"{operators[0]} {operation} {operators[1]} -> {output}")


file = open("input.txt", "r")
for line in file:
    line = line.strip()

    if len(line) == 0:
        read_gates = True
        continue

    if read_gates:
        parts = line.split(" ")

        gates[(parts[1], (parts[0], parts[2]))] = parts[4]

# for gate in gates:
#     print(gate)

s0 = find_gate_output("XOR", ("x00", "y00"))
if s0 != "z00":
    swap(s0, "z00")
print_gate("XOR", ("x00", "y00"), "z00")

carry = find_gate_output("AND", ("x00", "y00"))
print_gate("AND", ("x00", "y00"), carry)

for i in range(1, 45):
    # print(i)

    x = f"x{i:02d}"
    y = f"y{i:02d}"
    z = f"z{i:02d}"

    checker = find_gate_operator("XOR", carry, z)

    op1 = find_gate_output("XOR", (x, y))
    if checker is not None and op1 != checker:
        swap(op1, checker)
        op1 = checker
    print_gate("XOR", (x, y), op1)

    op2 = find_gate_output("XOR", (carry, op1))
    if op2 != z:
        swap(op2, z)
        op2 = z
    print_gate("XOR", (carry, op1), z)

    op3 = find_gate_output("AND", (x, y))
    print_gate("AND", (x, y), op3)

    op4 = find_gate_output("AND", (carry, op1))
    print_gate("AND", (carry, op1), op4)

    carry = find_gate_output("OR", (op3, op4))
    print_gate("OR", (op3, op4), carry)

    print()

print(",".join(sorted(swaps)))
