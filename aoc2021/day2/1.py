"""https://adventofcode.com/2021/day/2"""

testinput = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

with open("2/input.txt", "r") as f:
    data = f.read().split("\n")
#data = testinput.split("\n")

pos = [0, 0]
for line in data:
    try:
        cmd, dist = line.split(" ")
    except Exception:
        break
    if cmd == "forward":
        pos[0] += int(dist)
    elif cmd == "down":
        pos[1] += int(dist)
    elif cmd == "up":
        pos[1] -= int(dist)
    else:
        raise NotImplementedError

print(pos, pos[0] * pos[1])

