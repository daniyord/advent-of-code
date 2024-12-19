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
