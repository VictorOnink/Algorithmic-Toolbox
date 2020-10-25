# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10

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

def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18
    # Get the last digit of fibonacci number of n + 2
    cycle = pisano_cycle(10)
    period = len(cycle)
    # The last digit of the sum is the last digit of n+2 - 1
    return (cycle[(n+2) % period] - 1) % 10

if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
