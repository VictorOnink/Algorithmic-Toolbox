# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


def brute_force(points):
    if len(points) is 2:
        return distance_squared(points[0], points[2])
    else:
        min_distance = 1e99
        for count_1, point_1 in enumerate(points):
            for count_2, point_2 in enumerate(points[(count_1 + 1):]):
                dist = distance_squared(point_1, point_2)
                if dist < min_distance:
                    min_distance = dist
        return min_distance


def minimum_distance_squared(points):
    # Brute force attack if the number of points is small
    N = len(points)
    if N <= 3:
        return minimum_distance_squared_naive(points)

    mid = N // 2
    # Check distances for the total point list split in two
    d_first = minimum_distance_squared(points[:mid])
    d_last = minimum_distance_squared(points[mid:])
    d_min = min(d_first, d_last)






if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))
