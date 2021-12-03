import aoc2021.day1
import aoc2021.day2
import aoc2021.day3
import aoc2021.day4


def solve(day: int, part: int, data: list) -> int:
    if day == 1:
        return aoc2021.day1.solve(part, data)
    elif day == 2:
        return aoc2021.day2.solve(part, data)
    elif day == 3:
        return aoc2021.day3.solve(part, data)
    elif day == 4:
        return aoc2021.day4.solve(part, data)
    else:
        raise NotImplementedError
