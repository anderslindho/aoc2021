"""https://adventofcode.com/2021/day/1"""

testinput = """00100
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
01010"""

with open("3/input.txt", "r") as f:
    data = f.read().split("\n")
#data = testinput.split("\n")

bits = [[int(digit) for digit in line] for line in data]
rows = len(bits)
sums = [sum(x) for x in zip(*bits)]
print(sums, rows)

# 0 0 0 0 1 0 1 1 0 0 0 1
# 1 1 1 1 0 1 0 0 1 1 1 0

product = int('000010110001', 2) * int('111101001110', 2)
print(product)
