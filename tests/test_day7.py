import pytest

from aoc2021.day7 import solve

TEST_DATA = """\
16,1,2,0,4,2,7,1,2,14""".split(
    "\n"
)


@pytest.mark.parametrize(
    "part, expected",
    [
        (1, 37),
        (2, 168),
    ],
)
def test(part, expected):
    actual = solve(part, TEST_DATA)
    assert actual == expected
