from shared import get_input, number_to_digits, digits_to_number


def process(number):
    if number == 0:
        return [1]

    digits = number_to_digits(number)
    middle = len(digits) // 2

    if len(digits) % 2 == 0:
        return [digits_to_number(digits[0: middle]), digits_to_number(digits[middle:])]

    return [number * 2024]


numbers = get_input()

for i in range(0, 6):
    new_numbers = []
    for number in numbers:
        new_numbers += process(number)

    # print(new_numbers)

    numbers = new_numbers

    # print(f"{i+1}: {len(numbers)}: {numbers}")
    print(f"{i+1}: {len(numbers)}")
