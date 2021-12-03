"""https://adventofcode.com/2021/day/1"""

from ..utils import PACKAGE_DIR, read_data


def count_depth_increases2(numbers: list) -> int:
    increasing = 0
    sums = [
        sum(int(x) for x in triplet)
        for triplet in zip(numbers, numbers[1:], numbers[2:])
    ]
    for first, second in zip(sums, sums[1:]):
        if second > first:
            increasing += 1
    return increasing


if __name__ == "__main__":
    data = read_data(PACKAGE_DIR / "day1" / "input.txt")
    increases = count_depth_increases2(data)
    print(increases)
