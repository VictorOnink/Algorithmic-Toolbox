# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    values = [10, 5, 1]
    number = [0, 0, 0]
    for counter, coin in enumerate(values):
        while money >= coin:
            number[counter] += 1
            money -= coin
    return sum(number)

if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
