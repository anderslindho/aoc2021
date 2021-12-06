"""https://adventofcode.com/2021/day/5"""


def simulate_lanternfish(data, days) -> int:
    assert len(data) == 1
    days_left = {i: 0 for i in range(9)}
    for x in data[0].split(","):
        days_left[int(x)] += 1
    for _ in range(days):
        tmp = days_left[0]
        for i in range(8):
            days_left[i] = days_left[i + 1]
            if i == 6:
                days_left[i] += tmp
        days_left[8] = tmp
    return sum(days_left.values())


def solve(part: int, data: list) -> int:
    if part == 1:
        return simulate_lanternfish(data, 80)
    elif part == 2:
        return simulate_lanternfish(data, 256)
    else:
        raise NotImplementedError
