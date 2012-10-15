#!/usr/bin/python
__author__ = 'peter.vel'

data = []
file = open("data/matrix.txt")
lines = file.readlines()
for line in lines:
	line = line.strip()
	list = line.split(",")
	data.append([int(i) for i in list])

rows = len(data)-1
cols = len(data)-1

def shortest_path(x, y):
	if x == cols and y == rows:
		return data[x][y]

	best = 1000000000000
	if x < cols:
		best = shortest_path(x+1, y)

	if y < rows:
		option2 = shortest_path(x, y+1)
		if option2 < best:
			best = option2

	return data[x][y] + best

def main():
	print(shortest_path(0,0))

main()