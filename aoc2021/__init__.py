import sys

import aoc2021.day1
import aoc2021.day2
import aoc2021.day3
import aoc2021.day4
import aoc2021.day5
import aoc2021.day6
import aoc2021.day7


def solve(day: int, part: int, data: list) -> int:
    if day == 1:
        return aoc2021.day1.solve(part, data)
    elif day == 2:
        return aoc2021.day2.solve(part, data)
    elif day == 3:
        return aoc2021.day3.solve(part, data)
    elif day == 4:
        return aoc2021.day4.solve(part, data)
    elif day == 5:
        return aoc2021.day5.solve(part, data)
    elif day == 6:
        return aoc2021.day6.solve(part, data)
    elif day == 7:
        return aoc2021.day7.solve(part, data)
    else:
        print("Not a valid choice.")
        sys.exit(-1)
