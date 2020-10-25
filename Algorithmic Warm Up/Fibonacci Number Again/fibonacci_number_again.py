# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

def fibonacci_number(n):
    F = [0, 1]
    for count in range(1, n):
        F.append(F[-2] + F[-1])
    return F

def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

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
    return cycle[n % len(cycle)]

if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
    # for index in range(15):
    #     mod = 3
    #     str_format = (index, mod, fibonacci_number_again(index,mod))
    #     print('i = {}, m = {}, F_i mod m = {}'.format(*str_format))