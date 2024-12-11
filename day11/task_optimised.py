from shared import get_input, number_to_digits, digits_to_number
import time


def modify(dict, key, add):
    if not key in dict:
        dict[key] = 0

    dict[key] += add


def process(number):
    if number == 0:
        return [1]

    digits = number_to_digits(number)
    middle = len(digits) // 2

    if len(digits) % 2 == 0:
        return [digits_to_number(digits[0: middle]), digits_to_number(digits[middle:])]

    return [number * 2024]


numbers = {}
for number in get_input():
    modify(numbers, number, 1)

start = time.time()
for i in range(0, 75):
    temp = {}
    for number in numbers:
        for new_number in process(number):
            modify(temp, new_number, numbers[number])

    numbers = temp

    result = 0
    for number in numbers:
        result += numbers[number]

    # print(f"{i+1}: {result}: {numbers}")
    # print(f"{i+1}: {result}")

end = time.time()
print(f"{i+1}: {result}", f"{(end - start)*1000}ms")
