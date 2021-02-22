# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    coin_number = [0]
    coin_values = [1, 3, 4]
    for value in range(1, money+1):
        minimum = 1e99
        for coin in coin_values:
            if coin <= value:
                minimum = min(minimum, coin_number[value - coin] + 1)
        coin_number.append(minimum)
    return coin_number[-1]



if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
