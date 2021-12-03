"""https://adventofcode.com/2021/day/3"""

from ..utils import PACKAGE_DIR, read_data, convert_strbits_to_dec


def diagnostic_report(data):
    bits = [[int(digit) for digit in line] for line in data]
    rows = len(bits)
    sums = [sum(x) for x in zip(*bits)]

    epsilon_rate = [1 if (count > rows / 2) else 0 for count in sums]
    gamma_rate = [0 if x == 1 else 1 for x in epsilon_rate]

    return convert_strbits_to_dec(epsilon_rate), convert_strbits_to_dec(gamma_rate)


if __name__ == "__main__":
    data = read_data(PACKAGE_DIR / "day3" / "input.txt")
    gamma_rate, epsilon_rate = diagnostic_report(data)
    print(gamma_rate * epsilon_rate)
