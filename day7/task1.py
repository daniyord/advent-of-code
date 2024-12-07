def check_line(line):
    parts = line.split(":")

    check_total = int(parts[0])
    numbers = [int(x) for x in parts[1].strip().split(" ")]

    options = [[numbers[0]]]

    for number in numbers[1:]:
        for index in range(0, len(options)):
            option = options[index]

            new_option = option.copy()
            new_option.append("*")
            new_option.append(number)
            options.append(new_option)

            option.append("+")
            option.append(number)

    for option in options:
        total = option[0]

        for index in range(1, len(option), 2):
            op = option[index]

            if op == "+":
                total += option[index+1]
            if op == "*":
                total *= option[index+1]

        print(line, option, total, total == check_total)

        if total == check_total:
            # print(line, option)
            return True, check_total

    return False, None


result = []
with open('input_demo.txt', 'r') as file:
    for line in file:
        line = line.strip()

        is_ok, total = check_line(line)
        if is_ok:
            result.append(total)

print(sum(result))
