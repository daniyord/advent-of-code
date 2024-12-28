from shared import calculate_next

best_offers = {}


def calculate_prices(index, secret, depth):
    prev_price = secret % 10

    prices = []
    for _ in range(0, depth):
        secret = calculate_next(secret)

        price = secret % 10
        diff = price - prev_price

        prices.append((diff, price))

        if len(prices) >= 4:
            price1 = prices[-4]
            price2 = prices[-3]
            price3 = prices[-2]
            price4 = prices[-1]

            # print(price1, price2, price3, price4)

            key = f"{price1[0]}_{price2[0]}_{price3[0]}_{price4[0]}"

            if key not in best_offers:
                best_offers[key] = {}

            if index not in best_offers[key]:
                best_offers[key][index] = price4[1]

        prev_price = price

    return prices


result = []
file = open('input.txt', 'r')
for index, line in enumerate(file):
    calculate_prices(index, int(line.strip()), 2000)


max_price = None
for key in best_offers:

    price = 0
    for item in best_offers[key]:
        price += best_offers[key][item]

    if max_price is None or max_price < price:
        max_price = price


print(max_price)
