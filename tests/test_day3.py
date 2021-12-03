import pytest

from aoc2021.day3 import solve

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


@pytest.mark.parametrize(
    "part, expected",
    [
        (1, 198),
        (2, 230),
    ],
)
def test(part, expected):
    actual = solve(part, TEST_DATA)
    assert actual == expected
