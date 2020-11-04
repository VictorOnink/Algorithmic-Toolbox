# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    number_stops = 0
    current_index = 0
    last_stop_distance = 0
    # Add the final position to the list of stops
    stops.append(d)
    n = len(stops)
    # So long as we have not yet reached the end
    while current_index < n:
        # First check if the distance between the current position and the last fueling
        # position is less than m
        if stops[current_index] - last_stop_distance <= m:
            # If yes, increase the index by one
            current_index += 1
        # If the distance between the next set of stops is greater than m, then it is
        # impossible. Similarly, if current_index is still 0, then already the first
        # distance to travel is too great
        elif stops[current_index] - stops[current_index - 1] > m or current_index == 0:
            return -1
        # So, if the distance could hypothetically be crossed, then we must refuel at
        # current_index - 1 and we increase the stop counter by 1
        else:
            last_stop_distance = stops[current_index - 1]
            number_stops += 1
    return number_stops


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
