"""https://adventofcode.com/2021/day/2"""

from ..utils import PACKAGE_DIR, read_data


def calculate_position(data: list) -> tuple:
    pos = [0, 0]
    for line in data:
        cmd, dist = line.split(" ")
        if cmd == "forward":
            pos[0] += int(dist)
        elif cmd == "down":
            pos[1] += int(dist)
        elif cmd == "up":
            pos[1] -= int(dist)
        else:
            raise RuntimeError

    return pos[0], pos[1]


if __name__ == "__main__":
    data = read_data(PACKAGE_DIR / "day2" / "input.txt")
    dist, depth = calculate_position(data)
    print(dist * depth)
