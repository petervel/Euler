#!/usr/bin/python
__author__ = 'peter.vel'

class Sudoku:
	def __init__(self, name, known_values):
		self.name = name
		self.known_values = known_values
		self.numbers = []

	@staticmethod
	def read(file):
		numbers = []
		name = file.readline()
		for i in range(9):
			line = file.readline()
			line = line.strip()
			arr = list(line)
			numbers.append(arr)
		return Sudoku(name, numbers)

	@staticmethod
	def has_all_digits(set):
		found = [False] * 10
		for value in set:
			if value < 1 or value > 9 or found[value]:
				return False
			found[value] = True
		return True

	def check_row(self, row):
		set = [self.numbers[i][row] for i in range(1,10)]
		return Sudoku.has_all_digits(set)

	def check_col(self, col):
		set = [self.numbers[col][i] for i in range(1,10)]
		return Sudoku.has_all_digits(set)

	def check_block(self, x_offset, y_offset):
		set = []
		for x in range(x_offset * 3, (x_offset+1) * 3):
			for y in range(y_offset * 3, (y_offset+1) * 3):
				set.append(self.numbers[y][x])
		return Sudoku.has_all_digits(set)

	def is_valid(self):
		for i in range(1,10):
			if not self.check_row(i): return False
			if not self.check_col(i): return False
			if not self.check_block(i/3, i%3): return False
		return True

	def generate_row_solutions(self, row):
		numbers_left = range(1, 10)
		for i in row:
			if i != 0:
				numbers_left.remove(i)
				if len(numbers_left) == 0:
					return row

		first_empty = 0
		while row[first_empty] != 0:
			first_empty += 1

		rows = []
		for i in numbers_left:
			new_row = list(row)
			row[first_empty] = i
			rows.append(self.generate_row_solutions(new_row))

		return rows

	def solve(self):
		print("todo")
		#TODO: how do I brute-force this efficiently? :-/

	def get_top_left(self):
		string = ''.join(self.numbers[0][:3])
		return int(string)

def read_sudokus(filename):
	file = open(filename)
	list = []
	for i in range(50):
		sudoku = Sudoku.read(file)
		list.append(sudoku)
	file.close()
	return list

def main():
	sudokus = read_sudokus("data/sudoku.txt")
	for sudoku in sudokus:
		sudoku.solve()
	answer = sum(sudoku.get_top_left() for sudoku in sudokus)
	print answer

main()