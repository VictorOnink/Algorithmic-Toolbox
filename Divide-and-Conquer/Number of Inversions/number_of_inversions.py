# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions

def compute_mergestort(a):
    if len(a) == 1:
        return a, 0

    # Split the list a right down the middle
    middle = len(a) // 2

    # Count the number of inversions in the first and second half of the array
    first, first_count = compute_mergestort(a[:middle])
    last, last_count = compute_mergestort(a[middle:])

    # Now we need to merge the first and last lists into one sorted
    result, merge_inversions, i, j = [], 0, 0, 0
    while i < len(first) and j < len(last):
        if first[i] <= last[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(last[j])
            j += 1
            merge_inversions += len(first) - i
    result += first[i:]
    result += last[j:]

    # So result is the sorted version of original list a, and then the number
    # of inversions
    return result, first_count + last_count + merge_inversions
    
    
def compute_inversions(a):
    """
    This code counts the number of inversions
    """
    sort, inversions = compute_mergestort(a)
    return inversions


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))
