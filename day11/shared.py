def get_input():
    with open('input_demo.txt', 'r') as file:
        return [int(x) for x in file.read().split(" ")]


def number_to_digits(number):
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
