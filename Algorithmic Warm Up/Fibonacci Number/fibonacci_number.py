# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n
    print('compute F sub', n)
    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)

def fibonacci_number(n):
    assert 0 <= n <= 45
    F = [0, 1]
    for count in range(1, n):
        F.append(F[-2] + F[-1])
    return F[n]

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
