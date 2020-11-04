# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def which_is_best(candidate, max_value):
    if int(str(candidate)+str(max_value)) >= int(str(max_value)+str(candidate)):
        return candidate
    else:
        return max_value


def largest_number(numbers):
    order = []
    while len(numbers) > 0:
        max_value = numbers[0]
        for candidate in numbers:
            max_value = which_is_best(candidate, max_value)
        order.append(max_value)
        numbers.remove(max_value)
    order = [str(number) for number in order]
    return int(''.join(order))


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
