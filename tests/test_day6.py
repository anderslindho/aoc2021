import pytest

from aoc2021.day6 import solve

TEST_DATA = """\
3,4,3,1,2""".split(
    "\n"
)


@pytest.mark.parametrize(
    "part, expected",
    [
        (1, 5934),
        (2, 26984457539),
    ],
)
def test(part, expected):
    actual = solve(part, TEST_DATA)
    assert actual == expected
