import pytest

from aoc2021.day5 import solve

TEST_DATA = """\
""".split(
    "\n"
)


@pytest.mark.parametrize(
    "part, expected",
    [],
)
def test(part, expected):
    actual = solve(part, TEST_DATA)
    assert actual == expected
