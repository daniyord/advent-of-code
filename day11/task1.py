def get_input():
    with open('input.txt', 'r') as file:
        return file.read()


def number_to_digits(number):
    # print(number)

    digits = []

    while number > 0:
        digits.insert(0, number % 10)
        number = number // 10
    return digits


def digits_to_number(digits):
    number = 0

    for index, digit in enumerate(reversed(digits)):
        number += digit * 10 ** index

    return number


def process(number):
    if number == 0:
        return [1]

    digits = number_to_digits(number)
    middle = len(digits) // 2

    if len(digits) % 2 == 0:
        return [digits_to_number(digits[0: middle]), digits_to_number(digits[middle:])]

    return [number * 2024]


numbers = [int(x) for x in get_input().split(" ")]

for i in range(0, 25):
    new_numbers = []
    for number in numbers:
        new_numbers += process(number)

    # print(new_numbers)

    numbers = new_numbers

    print(i)

print(len(numbers))
