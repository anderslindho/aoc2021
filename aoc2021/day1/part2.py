"""https://adventofcode.com/2021/day/1"""

testinput = """199
200
208
210
200
207
240
269
260
263"""

with open("1/input.txt", "r") as f:
    data = f.read().split("\n")
#data = testinput.split("\n")

increasing = 0
sums = [sum(int(x) for x in triplet) for triplet in zip(data, data[1:], data[2:])]
for first, second in zip(sums, sums[1:]):
    if second > first:
        increasing += 1

print(increasing)
