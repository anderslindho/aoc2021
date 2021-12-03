from aoc2021.day3 import part1, part2

TEST_DATA = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".split(
    "\n"
)


def test_part1():
    actual = part1.solve(TEST_DATA)
    expected = 198
    assert actual == expected


def test_part2():
    actual = part2.solve(TEST_DATA)
    expected = 230
    assert actual == expected
