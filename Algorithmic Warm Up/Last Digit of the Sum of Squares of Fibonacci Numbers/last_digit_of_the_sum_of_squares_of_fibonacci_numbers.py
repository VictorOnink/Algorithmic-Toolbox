# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10

def pisano_cycle(m):
    # determine the period for mod m
    F = [0, 1]
    Fmod = [f % m for f in F]
    for count in range(1, m**2):
        F.append(F[-2] + F[-1])
        Fmod.append(F[-1]%m)
        if Fmod[-1] == 1 and Fmod[-2] == 0:
            cycle = Fmod[:-2]
            break
    # Get the mod value
    return cycle

def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    if n == 0:
        return 0
    else:
        # Get pisano cycle for mod 10
        cycle = pisano_cycle(10)
        period = len(cycle)
        # From proof by induction, it can be shown that Sum_n=1^k(F^2_n) = F_k*F_{k+1}
        # For proof, see https://proofwiki.org/wiki/Sum_of_Sequence_of_Squares_of_Fibonacci_Numbers
        # So, to get the last digit of the sum of squares, we just need the last digit of
        # F_n and F_{n+1}
        digit_n = cycle[n % period]
        digit_np = cycle[(n+1) % period]
        last_digit = (digit_n*digit_np) % 10
        return last_digit


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
