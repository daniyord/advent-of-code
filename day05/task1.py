from shared import get_input, check_rule

page_orders, rules = get_input()

result = 0
for rule in rules:
    is_ok, _, _ = check_rule(rule, page_orders)

    if is_ok:
        result += int(rule[len(rule) // 2])

print(result)
