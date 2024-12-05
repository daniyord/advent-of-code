from shared import get_input

page_orders, rules = get_input()


def check_rule(rule, page_orders):
    for index, rule_part in enumerate(rule):
        for check_index in range(index+1, len(rule)):
            if rule_part not in page_orders or rule[check_index] not in page_orders[rule_part]:
                return False

    return True


result = 0
for rule in rules:
    if check_rule(rule, page_orders):
        result += int(rule[len(rule) // 2])

print(result)
