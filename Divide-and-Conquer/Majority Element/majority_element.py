# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element_recursive(elements):
    # assert len(elements) <= 10 ** 5

    def recursive_majority(low, high):
        # In this case we are looking at simplest case where we look at just a single element
        if low + 1 == high:
            return elements[low]

        # Otherwise, we now look at getting the majority of the left and right side
        middle = low + (high - low) // 2
        left = recursive_majority(low, middle)
        right = recursive_majority(middle + 1, high)

        # Check for agreement of the left and right side of the
        if left == right:
            return left

        # Else, see which of the two is more frequent
        left_count = elements[:middle].count(left)
        right_count = elements[middle:].count(right)
        return left if left_count > right_count else right

    most_common = recursive_majority(0, len(elements) - 1)
    if elements.count(most_common) > len(elements) // 2:
        return 1
    else:
        return 0

def majority_element(elements):
    n=len(elements)
    elements.sort()
    count = 0
    majority = elements[0]
    for e in elements:
        if e == majority:
            count += 1
        else:
            majority = e
            count = 1
        if count > n // 2:
            return 1
    return 0



if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
