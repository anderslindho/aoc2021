"""https://adventofcode.com/2021/day/2"""

from dataclasses import dataclass


@dataclass
class Submarine:
    horiz_pos: int
    depth: float

    def move(self, direction: str, distance: int) -> None:
        if direction == "forward":
            self.horiz_pos += distance
        elif direction == "down":
            self.depth += distance
        elif direction == "up":
            self.depth -= distance
        else:
            raise LookupError


@dataclass
class MoreComplicatedSubmarine(Submarine):
    aim: int

    def move(self, direction: str, distance: int) -> None:
        if direction == "forward":
            self.horiz_pos += distance
            self.depth += self.aim * distance
        elif direction == "down":
            self.aim += distance
        elif direction == "up":
            self.aim -= distance
        else:
            raise LookupError


def find_new_position(sub: Submarine, data: list) -> tuple:
    for command, distance in (line.split(" ") for line in data):
        sub.move(command, int(distance))
    return sub.horiz_pos, sub.depth


def solve(part: int, data: list) -> int:
    if part == 1:
        dist, depth = find_new_position(Submarine(0, 0), data)
    elif part == 2:
        dist, depth = find_new_position(MoreComplicatedSubmarine(0, 0, 0), data)
    else:
        raise NotImplementedError
    return dist * depth
