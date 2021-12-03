"""https://adventofcode.com/2021/day/2"""

from dataclasses import dataclass
import logging
import pathlib

from ..utils import read_data

MODULE_DIR = pathlib.Path(__file__).parent

TEST_DATA = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2""".split("\n")

logger = logging.getLogger(__name__)


@dataclass
class Submarine:
    horiz_pos: int
    depth: float
    aim: int


def calculate_position(commands: list) -> int:
    sub = Submarine(0, 0, 0)
    for idx, cmd in enumerate(commands, 1):
        order, magnitude = cmd.split(" ")
        magnitude = int(magnitude)
        if order == "forward":
            sub.horiz_pos += magnitude
            sub.depth += (sub.aim * magnitude)
        elif order == "down":
            sub.aim += magnitude
        elif order == "up":
            sub.aim -= magnitude
        else:
            raise RuntimeError
        logging.info(idx, cmd)
        logging.debug(sub)

    return sub.horiz_pos, sub.depth
        


def test_calculate_position():
    dist, depth = calculate_position(TEST_DATA)
    actual = dist * depth
    expected = 900
    assert actual == expected


if __name__ == "__main__":
    data = read_data(MODULE_DIR / "input.txt")
    dist, depth = calculate_position(data)
    print(dist * depth)
