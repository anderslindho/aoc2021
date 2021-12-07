"""https://adventofcode.com/2021/day/5"""

import re
from dataclasses import dataclass

import numpy as np


def parse(data) -> list:
    return [Line.from_str(*line.split(" -> ")) for line in data]


def str_to_tuple(coords: str) -> tuple:
    return tuple(map(int, coords.split(",")))


def find_largest_int(lines) -> int:
    return max(map(int, re.findall(r"\d+", "".join(lines))))


class SquareBoard:
    def __init__(self, dimensions: int) -> None:
        self.dimensions = dimensions
        self.counts = np.zeros((dimensions + 1, dimensions + 1), int)

    def draw(self, line, include_diagonals=False):
        if line.is_vertical():
            smallest = min(line.first.y, line.second.y)
            largest = max(line.first.y, line.second.y)
            self.counts[smallest : largest + 1, line.first.x] += 1
        elif line.is_horizontal():
            smallest = min(line.first.x, line.second.x)
            largest = max(line.first.x, line.second.x)
            self.counts[line.first.y, smallest : largest + 1] += 1
        elif line.is_diagonal() and include_diagonals:
            pass

    def count_intersections(self):
        return np.count_nonzero(self.counts >= 2)


@dataclass
class Point:
    x: int
    y: int

    @classmethod
    def from_str(cls, coords: str):
        return cls(*str_to_tuple(coords))

    @property
    def xy(self):
        return self.x, self.y


class Line:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    @classmethod
    def from_str(cls, first, second):
        return cls(Point.from_str(first), Point.from_str(second))

    @property
    def points(self):
        return self.first, self.second

    @property
    def delta_x(self):
        return max(self.first.x, self.second.x) - min(self.first.x, self.second.x)

    @property
    def delta_y(self):
        return max(self.first.y, self.second.y) - min(self.first.y, self.second.y)

    def is_vertical(self) -> bool:
        return self.points[0].x == self.points[1].x

    def is_horizontal(self) -> bool:
        return self.points[0].y == self.points[1].y

    def is_diagonal(self) -> bool:
        return self.delta_y == self.delta_x

    def get_highest_value(self) -> int:
        p1, p2 = self.points
        return max(*p1.xy, *p2.xy)


def count_intersections(data: list, diagonals=False) -> int:
    lines = parse(data)
    board = SquareBoard(dimensions=max(x.get_highest_value() for x in lines))
    for line in lines:
        board.draw(line, include_diagonals=diagonals)
    return board.count_intersections()


def solve(part: int, data: list) -> int:
    if part == 1:
        return count_intersections(data)
    elif part == 2:
        return count_intersections(data, diagonals=True)
    else:
        raise NotImplementedError
