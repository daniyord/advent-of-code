def get_input(filename):
    file = open(filename, 'r')

    designs = []
    for index, line in enumerate(file):
        line = line.strip()

        if index == 0:
            patterns = [x.strip() for x in line.split(",")]

        if index > 1:
            designs.append(line)

    return (patterns, designs)


def find_patterns(design, patterns):
    # print(design)
    checks = {}

    for pattern in patterns:
        if design.startswith(pattern):
            checks[len(pattern)] = 1

    # print(checks)
    while len(checks) > 0 and min(checks) < len(design):
        next = min(checks)

        for pattern in patterns:
            if design[next:].startswith(pattern):
                new_length = next + len(pattern)

                if not new_length in checks:
                    checks[new_length] = 0

                checks[new_length] += checks[next]

        del checks[next]
        # print(checks)

    if len(design) in checks:
        # print("success:", checks[len(design)])
        # print()
        return checks[len(design)]

    # print("fail:")
    # print()
    return 0
