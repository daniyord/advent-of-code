from shared import calculate_next


def calculate_prices(secret, depth):
    prev_price = secret % 10

    prices = []
    for _ in range(0, depth):
        secret = calculate_next(secret)

        price = secret % 10
        diff = price - prev_price

        prices.append((diff, price))

        prev_price = price

    return prices


print(calculate_prices(123, 2000))


# result = []
# file = open('input_demo.txt', 'r')
# for line in file:
#     print(calculate_prices(int(line.strip()), 10))
#     exit(0)
