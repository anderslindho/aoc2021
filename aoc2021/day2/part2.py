"""https://adventofcode.com/2021/day/2"""

import logging
from dataclasses import dataclass

from ..utils import PACKAGE_DIR, read_data

logger = logging.getLogger(__name__)


@dataclass
class Submarine:
    horiz_pos: int
    depth: float
    aim: int


def calculate_position2(commands: list) -> tuple:
    sub = Submarine(0, 0, 0)
    for idx, cmd in enumerate(commands, 1):
        order, magnitude = cmd.split(" ")
        magnitude = int(magnitude)
        if order == "forward":
            sub.horiz_pos += magnitude
            sub.depth += sub.aim * magnitude
        elif order == "down":
            sub.aim += magnitude
        elif order == "up":
            sub.aim -= magnitude
        else:
            raise RuntimeError
        logging.info(f"{idx}, {cmd}")
        logging.debug(sub)

    return sub.horiz_pos, sub.depth


def solve(data: list) -> int:
    dist, depth = calculate_position2(data)
    return dist * depth


if __name__ == "__main__":
    data = read_data(PACKAGE_DIR / "day2" / "input.txt")
    print(solve(data))
