"""https://adventofcode.com/2021/day/1"""

from ..utils import PACKAGE_DIR, read_data


def count_depth_increases(numbers: list) -> int:
    increasing = 0
    for first, second in zip(numbers, numbers[1:]):
        if int(second) > int(first):
            increasing += 1
    return increasing


if __name__ == "__main__":
    data = read_data(PACKAGE_DIR / "day1" / "input.txt")
    increases = count_depth_increases(data)
    print(increases)
