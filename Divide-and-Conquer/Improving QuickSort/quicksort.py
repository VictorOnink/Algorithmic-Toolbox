# python3

from random import randint


def partition3(array: list, left: int, right: int):
    # We take the first element as our pivot
    pivot_value = array[left]
    start = index = left
    end = right
    while index <= end:
        if array[index] < pivot_value:
            array[index], array[start] = array[start], array[index]
            start += 1
            index += 1
        elif array[index] == pivot_value:
            index+=1
        else:
            array[index], array[end] = array[end], array[index]
            end-=1
    return start, end


def randomized_quick_sort(array: list, left: int, right: int):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    start, end = partition3(array, left, right)
    randomized_quick_sort(array, left, start - 1)
    randomized_quick_sort(array, end + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
