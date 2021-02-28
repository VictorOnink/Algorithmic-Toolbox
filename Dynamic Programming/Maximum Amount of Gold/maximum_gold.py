# python3

from sys import stdin
import numpy as np


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    # Create an array with dimensions (number of weights, capacity + 1)
    max_cap = np.zeros((len(weights), capacity + 1), dtype=np.int32)
    # Looping through all the different nodes of max_cap
    for w in range(0, len(weights)):
        for cap in range(1, capacity + 1):
            if weights[w] > cap:
                max_cap[w, cap] = max_cap[w - 1, cap]
            else:
                max_cap[w, cap] = max(max_cap[w - 1, cap], weights[w] + max_cap[w - 1, cap - weights[w]])
    return max_cap[w, cap]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
