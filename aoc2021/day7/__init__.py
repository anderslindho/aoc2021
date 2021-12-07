"""https://adventofcode.com/2021/day/7"""

import operator
from functools import reduce


def increasing_sum(val: int) -> int:
    return reduce(operator.add, range(1, val + 1), 0)


def find_horizontal_alignment_with_minimal_fuel_consumption(
    data, increasing_cost: bool = False
) -> int:
    coords = [x for x in map(int, data[0].split(","))]
    lowest = None
    for i in range(min(coords), max(coords)):
        if not increasing_cost:
            diff = [abs(x - i) for x in coords]
        else:
            diff = [increasing_sum(abs(x - i)) for x in coords]
        diff_sum = sum(diff)
        if lowest is None or diff_sum < lowest:
            lowest = diff_sum

    return lowest


def solve(part: int, data: list) -> int:
    if part == 1:
        return find_horizontal_alignment_with_minimal_fuel_consumption(data)
    elif part == 2:
        return find_horizontal_alignment_with_minimal_fuel_consumption(
            data, increasing_cost=True
        )
    else:
        raise NotImplementedError
