import pytest

from aoc2021.day2 import solve

TEST_DATA = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2""".split(
    "\n"
)


@pytest.mark.parametrize(
    "part, expected",
    [
        (1, 150),
        (2, 900),
    ],
)
def test(part, expected):
    actual = solve(part, TEST_DATA)
    assert actual == expected
