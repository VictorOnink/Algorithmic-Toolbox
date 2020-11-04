# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')

def compute_optimal_points(segments):
    # sort all the segments according to the end part of the segment
    sorted_segments = sorted(segments, key=lambda segment: segment.end)
    # first point will be the end of the first segment
    point = sorted_segments[0].end
    point_list = [point]

    for segment in sorted_segments:
        # Basically, if a point is not within a segment, then we need to
        # add a new point as far to the right as possible, which works
        # since all the segments are sorted according to their end point
        if segment.start > point or point > segment.end:
            point = segment.end
            point_list.append(point)
    return point_list


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
