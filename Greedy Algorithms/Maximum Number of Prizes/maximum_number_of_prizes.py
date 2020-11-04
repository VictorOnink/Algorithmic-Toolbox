# python3

def compute_optimal_summands_naive(n):
    # This algorithm works, but it turns out that it is too slow for large numbers
    assert 1 <= n <= 10 ** 9
    summands = []

    integer = 1

    while n > 0:
        remainder = n - integer
        if remainder >= 0 and remainder not in summands and remainder != integer:
            summands.append(integer)
            n = remainder
            integer += 1
        else:
            summands.append(n)
            n = 0
    return summands


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    integer = 1
    total = 0

    while total + integer <= n:
        total += integer
        summands.append(integer)
        integer += 1
    # To the last element, add the difference between n and the sum of integers up to that point
    summands[-1] += n - total
    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
