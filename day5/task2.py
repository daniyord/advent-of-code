from shared import get_input, check_rule

page_orders, rules = get_input()


def fix_rule(rule, check_index, error_index):
    rule.insert(check_index, rule[error_index])
    rule.pop(error_index+1)

    is_ok, check_index, error_index = check_rule(rule, page_orders)
    if not is_ok:
        fix_rule(rule, check_index, error_index)


result = 0
for rule in rules:
    is_ok, check_index, error_index = check_rule(rule, page_orders)

    if not is_ok:
        fix_rule(rule, check_index, error_index)
        result += int(rule[len(rule) // 2])

print(result)
