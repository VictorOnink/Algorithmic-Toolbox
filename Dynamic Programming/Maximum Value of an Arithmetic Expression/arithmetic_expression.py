# python3
import numpy as np
import re
import math

def operation(a, b, op):
    if op is '+':
        return a + b
    elif op is '-':
        return a - b
    elif op is 'x' or op is '*':
        return a * b


def determine_min_max_value(min_Matrix, max_Matrix, i, j, operator):
    MIN, MAX = 1e99, -1e99
    # Now we cycle through all the various options
    for ind in range(i, j):
        a_1 = operation(min_Matrix[i][ind], min_Matrix[ind + 1][j], operator[ind])
        a_2 = operation(min_Matrix[i][ind], max_Matrix[ind + 1][j], operator[ind])
        a_3 = operation(max_Matrix[i][ind], min_Matrix[ind + 1][j], operator[ind])
        a_4 = operation(max_Matrix[i][ind], max_Matrix[ind + 1][j], operator[ind])
        MIN, MAX = min(MIN, a_1, a_2, a_3, a_4), max(MAX, a_1, a_2, a_3, a_4)
    return MIN, MAX

def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29
    # We load the expressions, and assume that in all the test cases we have that we are dealing with single digit
    # integers
    digits = re.split('\+|\-|x|\*', dataset)
    D = len(digits)
    operators = re.split('0|1|2|3|4|5|6|7|8|9', dataset)
    operators[:] = (value for value in operators if value != '')

    # Initializing the min and max matrices
    min_Matrix = np.zeros(shape=(D, D), dtype=float)
    max_Matrix = np.zeros(shape=(D, D), dtype=float)

    for ii in range(D):
        min_Matrix[ii, ii] = digits[ii]
        max_Matrix[ii, ii] = digits[ii]

    # Now actually looping through all the different bracket options to get the max possible value
    for index_1 in range(1, D):
        for index_2 in range(0, D - index_1):
            index_3 = index_1 + index_2
            min_Matrix[index_2, index_3], max_Matrix[index_2, index_3] = determine_min_max_value(min_Matrix, max_Matrix,
                                                                                                 index_2, index_3,
                                                                                                 operators)
    return int(max_Matrix[0][D - 1])


if __name__ == "__main__":
    print(find_maximum_value(input()))
