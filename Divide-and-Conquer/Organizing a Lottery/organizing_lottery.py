# python3
from sys import stdin
from bisect import bisect_left, bisect_right


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover(starts, ends, points):
    # first, getting a list containing all the start, end and points coordinates
    master_list = []
    for i in range(len(starts)):
        master_list.append((starts[i], 'L'))
        master_list.append((ends[i], 'R'))
    for i in points:
        master_list.append((int(i), 'P'))
    master_list.sort()

    # Now, we go through the master list and for each point we come across, we count the number of segments that have
    # been 'opened' but not yet 'closed'
    segment_count, count_per_point = 0, dict()
    for tup in master_list:
        if tup[1] == 'L':
            segment_count += 1
        elif tup[1] == 'R':
            segment_count -= 1
        elif tup[1] == 'P':
            count_per_point[tup[0]] = segment_count

    # Getting then number of segments that each point falls in
    counts = [0] * len(points)
    for ind, p in enumerate(points):
        counts[ind] += count_per_point[p]
    return counts



if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
