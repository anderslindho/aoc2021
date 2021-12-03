from aoc2021.day1.part1 import count_depth_increases
from aoc2021.day1.part2 import count_depth_increases2

TEST_DATA = """\
199
200
208
210
200
207
240
269
260
263""".split(
    "\n"
)


def test_part1():
    actual = count_depth_increases(TEST_DATA)
    expected = 7
    assert actual == expected


def test_part2():
    actual = count_depth_increases2(TEST_DATA)
    expected = 5
    assert actual == expected
