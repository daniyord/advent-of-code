def get_input():
    page_orders = {}
    rules = []

    rules_mode = False

    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip()

            if len(line) == 0:
                rules_mode = True

            elif not rules_mode:
                parts = line.split("|")
                if parts[0] in page_orders:
                    page_orders[parts[0]].append(parts[1])
                else:
                    page_orders[parts[0]] = [parts[1]]

            else:
                parts = line.split(",")
                rules.append(parts)

    return (page_orders, rules)


def check_rule(rule, page_orders):
    for index, rule_part in enumerate(rule):
        for check_index in range(index+1, len(rule)):
            if rule_part not in page_orders or rule[check_index] not in page_orders[rule_part]:
                return (False, index, check_index)

    return (True, -1, -1)
