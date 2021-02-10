# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    # # Setting the initial range of indices to check
    start, end = 0, len(keys) - 1
    while start <= end:
        middle = start + (end - start) // 2
        if keys[middle] == query:
            return middle
        elif query < keys[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1

if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
