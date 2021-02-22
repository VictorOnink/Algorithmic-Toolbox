# python3
import numpy as np

def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    len1, len2, len3 = len(first_sequence), len(second_sequence), len(third_sequence)

    # Creating an array for lcs
    LCS = np.zeros((len1 + 1, len2 + 1, len3 + 1), dtype=np.int)

    # Going through the table, determining the LCS for each point
    for l1 in range(1, len1 + 1):
        for l2 in range(1, len2 + 1):
            for l3 in range(1, len3 + 1):
                if first_sequence[l1 - 1] == second_sequence[l2 - 1] == third_sequence[l3 - 1]:
                    LCS[l1, l2, l3] = LCS[l1 - 1, l2 - 1, l3 - 1] + 1
                else:
                    LCS[l1, l2] = max(LCS[l1 - 1, l2, l3], LCS[l1, l2 - 1, l3], LCS[l1, l2, l3 - 1])
    return LCS[l1, l2, l3]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
