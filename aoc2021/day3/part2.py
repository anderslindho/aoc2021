"""https://adventofcode.com/2021/day/3"""

import logging

from ..utils import PACKAGE_DIR, convert_strbits_to_dec, read_data

logger = logging.getLogger(__name__)


def calculate_ratings(numbers: list, verbose: bool = False) -> tuple:
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    h2_gen_rat = calculate_oxygen_generator_rating(numbers)
    co2_scrub_rat = calculate_co2_scrubber_rating(numbers)
    return convert_strbits_to_dec(h2_gen_rat), convert_strbits_to_dec(co2_scrub_rat)


def calculate_co2_scrubber_rating(numbers: list) -> int:
    least_common_bits = ""
    nbr_of_bits = len(numbers[0])
    for i in range(nbr_of_bits):
        nbrs_left = len(numbers)
        logger.debug(f"{nbrs_left}, {least_common_bits}")
        ones = 0
        for seq in numbers:
            ones += int(seq[i])
        if ones >= nbrs_left / 2:
            least_common_bits += "0"
        else:
            least_common_bits += "1"
        numbers = [x for x in numbers if x.startswith(least_common_bits)]
        if len(numbers) == 1:
            break
    logger.debug(numbers)
    assert len(numbers) == 1
    return numbers[0]


def calculate_oxygen_generator_rating(numbers: list) -> int:
    most_common_bits = ""
    nbr_of_bits = len(numbers[0])
    for i in range(nbr_of_bits):
        nbrs_left = len(numbers)
        logger.debug(f"{nbrs_left}, {most_common_bits}")
        ones = 0
        for seq in numbers:
            ones += 1 if seq[i] == "1" else 0
        if ones >= nbrs_left / 2:
            most_common_bits += "1"
        else:
            most_common_bits += "0"
        numbers = [x for x in numbers if x.startswith(most_common_bits)]
    logger.debug(numbers)
    assert len(numbers) == 1
    return numbers[0]


if __name__ == "__main__":
    data = read_data(PACKAGE_DIR / "day3" / "input.txt")
    h2_gen_rat, co2_scrub_rat = calculate_ratings(data)
    print(h2_gen_rat * co2_scrub_rat)
