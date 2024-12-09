from itertools import repeat


def get_input():
    with open('input.txt', 'r') as file:
        input = file.readline().strip()

        mode = 'digit'
        file_id = 0

        symbols = []
        for digit in input:
            if mode == 'digit':
                symbols.extend(repeat(str(file_id), int(digit)))
                mode = 'space'
                file_id += 1
                continue
            if mode == 'space':
                symbols.extend(repeat('.', int(digit)))
                mode = 'digit'
                continue

        return symbols
