#!/usr/bin/python
__author__ = 'peter.vel'

class Sudoku:
	@staticmethod
	def read(file):
		return Sudoku()

def read_sudokus(filename):
	file = open(filename)
	sudoku = Sudoku.read(file)
	file.close()

def main():
	read_sudokus("data/sudoku.txt")

main()