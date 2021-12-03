from aoc2021.day1 import part1, part2

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
    actual = part1.solve(TEST_DATA)
    expected = 7
    assert actual == expected


def test_part2():
    actual = part2.solve(TEST_DATA)
    expected = 5
    assert actual == expected
