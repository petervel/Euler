#!/usr/bin/python
__author__ = 'peter.vel'

data = []
solution = []

file = open("data/matrix.txt")
lines = file.readlines()
for line in lines:
	line = line.strip()
	list = line.split(",")
	data.append([int(i) for i in list])
	solution.append([0] * len(list))

rows = len(data)-1
cols = len(data)-1

def calc():
	for row in range(rows+1):
		for col in range(cols+1):
			shortest = 0
			if row != 0:
				above = solution[row-1][col]
				shortest = above
			if col != 0:
				left = solution[row][col-1]
				if shortest == 0 or left < shortest:
					shortest = left
			solution[row][col] = shortest + data[row][col]
	return solution[rows][cols]

def main():
	print(calc())

main()