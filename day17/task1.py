from shared import calculate, get_input

r_a, r_b, r_c, code = get_input("input_demo2.txt")
output = calculate(r_a, r_b, r_c, code)
print(",".join([str(x) for x in output]))
