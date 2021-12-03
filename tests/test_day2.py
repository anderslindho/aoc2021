from aoc2021.day2 import part1, part2

TEST_DATA = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2""".split(
    "\n"
)


def test_part1():
    actual = part1.solve(TEST_DATA)
    expected = 150
    assert actual == expected


def test_part2():
    actual = part2.solve(TEST_DATA)
    expected = 900
    assert actual == expected
