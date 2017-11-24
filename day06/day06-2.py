import re

f = open('day06.txt', 'r')
inputs = [x.strip('\n') for x in f.readlines()]
f.close()

def toggle(grid, row_1, col_1, row_2, col_2):
	for i in range(row_1, row_2 + 1):
		for j in range(col_1, col_2 + 1):
			grid[i][j] += 2

def on_off(grid, row_1, col_1, row_2, col_2, on_off):
	for i in range(row_1, row_2 + 1):
		for j in range(col_1, col_2 + 1):
			if on_off == 1:
				grid[i][j] += 1
			elif grid[i][j] > 0:
				grid[i][j] -= 1

n = 1000
grid = [[0 for col in range(n)] for row in range(n)]
for input in inputs:
	tog = re.match(r"toggle (\d+),(\d+) through (\d+),(\d+)", input)
	if tog:
		toggle(grid, int(tog.group(1)), int(tog.group(2)), int(tog.group(3)),
		       int(tog.group(4)))

	on = re.match(r"turn on (\d+),(\d+) through (\d+),(\d+)", input)
	if on:
		on_off(grid, int(on.group(1)), int(on.group(2)), int(on.group(3)), int(on.group(4)), 1)
	
	off = re.match(r"turn off (\d+),(\d+) through (\d+),(\d+)", input)
	if off:
		on_off(grid, int(off.group(1)), int(off.group(2)), int(off.group(3)), int(off.group(4)), 0)

print(sum([sum(x) for x in grid]))
