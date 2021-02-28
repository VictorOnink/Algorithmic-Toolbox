# python3

from itertools import product
from sys import stdin
import numpy as np


def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)
    total_value = sum(values)
    if len(values) < 3:
        # If we have less than three items, then it is impossible to create three groups of equal value
        return 0
    elif total_value % 3 is not 0:
        # If the total value is not divisible by three, it is also not possible to create three groups of equal value
        return 0
    else:
        # So we need to check if we can create three partitions, all with a total value values
        partition_value = np.zeros((len(values) + 1, (total_value // 3) + 1))

        # Loop through all the cells
        for souvenier in range(0, len(values)):
            for capacity in range(0, partition_value.shape[1]):
                if values[souvenier] > capacity:
                    partition_value[souvenier, capacity] = partition_value[souvenier - 1, capacity]
                else:
                    partition_value[souvenier, capacity] = max(partition_value[souvenier - 1, capacity],
                                                               values[souvenier] + partition_value[souvenier - 1, capacity - values[souvenier]])
        # Check how many partitions we have that have a value equal to total_value // 3
        count = np.sum(partition_value >= total_value // 3)
        if count >= 3:
            return 1
        else:
            return 0



if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
