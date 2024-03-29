from argparse import ArgumentParser

from aoc2021 import solve
from aoc2021.utils import PACKAGE_DIR, read_data


def main(day: int):
    data = read_data(PACKAGE_DIR / f"day{day}" / "input.txt")
    print(f"Day {day}")
    day = int(day)
    for part in (1, 2):
        try:
            solution = solve(day, part, data)
        except NotImplementedError:
            solution = "Unsolved"
        print(f"The solution to part {part} is: {solution}")


parser = ArgumentParser()
parser.add_argument("day")
args = parser.parse_args()
main(**vars(args))
