# python3


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    operation_number = [0, 0]
    intermediates = [[1], [1]]
    for number in range(2, n + 1):
        minimum = 1e99
        # Number of steps for +1
        if operation_number[number - 1] + 1 < minimum:
            minimum = operation_number[number - 1] + 1
            path = intermediates[number - 1] + [number]
            inter = number - 1
        # Check if integer is divisible by 2
        if number % 2 is 0:
            if operation_number[number // 2] + 1 < minimum:
                minimum = operation_number[number // 2] + 1
                path = intermediates[number // 2] + [number]
        # Check if integer is divisible by 3
        if number % 3 is 0:
            if operation_number[number // 3] + 1 < minimum:
                minimum = operation_number[number // 3] + 1
                path = intermediates[number // 3] + [number]
        operation_number.append(minimum)
        intermediates.append(path)
    return intermediates[-1]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
