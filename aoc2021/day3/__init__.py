"""https://adventofcode.com/2021/day/3"""

import operator
from functools import reduce

from ..utils import convert_strbits_to_dec


def power_consumption(data: list) -> int:
    bits = [[int(digit) for digit in line] for line in data]
    sums = [sum(x) for x in zip(*bits)]

    epsilon_rate = [1 if (count > len(bits) / 2) else 0 for count in sums]
    gamma_rate = [0 if x == 1 else 1 for x in epsilon_rate]

    return reduce(operator.mul, map(convert_strbits_to_dec, (epsilon_rate, gamma_rate)))


def life_support_rating(numbers: list) -> int:
    h2_gen_rat = calculate_oxygen_generator_rating(numbers)
    co2_scrub_rat = calculate_co2_scrubber_rating(numbers)
    return reduce(
        operator.mul,
        (convert_strbits_to_dec(h2_gen_rat), convert_strbits_to_dec(co2_scrub_rat)),
    )


def calculate_co2_scrubber_rating(numbers: list) -> int:
    least_common_bits = ""
    for i in range(len(numbers[0])):
        ones = sum(int(seq[i]) for seq in numbers)
        least_common_bits += "0" if ones >= len(numbers) / 2 else "1"
        numbers = [x for x in numbers if x.startswith(least_common_bits)]
        if len(numbers) == 1:
            break
    else:
        raise RuntimeError
    return numbers[0]


def calculate_oxygen_generator_rating(numbers: list) -> int:
    most_common_bits = ""
    for i in range(len(numbers[0])):
        ones = sum(int(seq[i]) for seq in numbers)
        most_common_bits += "1" if ones >= len(numbers) / 2 else "0"
        numbers = [x for x in numbers if x.startswith(most_common_bits)]
    assert len(numbers) == 1
    return numbers[0]


def solve(part: int, data: list) -> int:
    if part == 1:
        return power_consumption(data)
    elif part == 2:
        return life_support_rating(data)
    else:
        raise NotImplementedError
