import pytest

from aoc2021.day1 import solve

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


@pytest.mark.parametrize(
    "part, expected",
    [
        (1, 7),
        (2, 5),
    ],
)
def test(part, expected):
    actual = solve(part, TEST_DATA)
    assert actual == expected
