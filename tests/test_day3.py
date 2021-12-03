from aoc2021.day3.part1 import diagnostic_report
from aoc2021.day3.part2 import calculate_ratings

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
01010""".split("\n")


def test_diagnostic_report():
    eps_rate, gamma_rate = diagnostic_report(TEST_DATA)
    actual = eps_rate * gamma_rate
    expected = 198
    assert actual == expected


def test_calculate_position():
    h2_rat, co2_rat = calculate_ratings(TEST_DATA)
    actual = h2_rat * co2_rat
    expected = 230
    assert actual == expected
