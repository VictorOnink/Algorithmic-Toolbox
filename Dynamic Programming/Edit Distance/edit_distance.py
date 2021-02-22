# python3
import numpy as np


def edit_distance(first_string, second_string):
    len1, len2 = len(first_string), len(second_string)
    # Creating our 2D grid giving the edit distance for all the characters
    dist = np.zeros((len1 + 1, len2 + 1), dtype='int32')
    # Setting the first row and column equal to the index value
    for i in range(len1 + 1):
        dist[i, 0] = i
    for i in range(len2 + 1):
        dist[0, i] = i
    edit = 0
    for l1 in range(1, len1 + 1):
        for l2 in range(1, len2 + 1):
            if first_string[l1 - 1] is second_string[l2 - 1]:
                edit = 0
            else:
                edit = 1
            dist[l1][l2] = min(min(dist[l1 - 1, l2], dist[l1, l2 - 1]) + 1, dist[l1 - 1, l2 - 1] + edit)
    return dist[len1, len2]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
