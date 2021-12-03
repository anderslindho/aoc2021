from aoc2021.day2.part1 import calculate_position
from aoc2021.day2.part2 import calculate_position2

TEST_DATA = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2""".split("\n")


def test_calculate_position():
    dist, depth = calculate_position(TEST_DATA)
    actual = dist * depth
    expected = 150
    assert actual == expected


def test_calculate_position2():
    dist, depth = calculate_position2(TEST_DATA)
    actual = dist * depth
    expected = 900
    assert actual == expected
