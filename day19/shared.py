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
    print(design)
    checks = {}

    for pattern in patterns:
        if design.startswith(pattern):
            checks[pattern] = len(pattern)

    # print(checks)
    # print()

    border = 0
    while len(checks) > 0:
        border += 1

        if border == 10:
            break

        new_checks = {}

        for check in checks:
            total = checks[check]

            for pattern in patterns:
                if design[total:].startswith(pattern):
                    if total + len(pattern) >= len(design):
                        return True

                    # t = list(check[0])
                    # t.append(pattern)

                    # print(len(design), check[1] + len(pattern))
                    new_checks[check + pattern] = total + len(pattern)

        # print(checks)

        # if len(new_checks) > 45:
        #     return False

        checks = new_checks

        print(checks)
        print()

    return False
