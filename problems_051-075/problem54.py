#!/usr/bin/python
__author__ = 'peter.vel'

class Hand:
	def __init__(self, cards):
		self.cards = cards

	def __cmp__(self, other):
		return 1

class Round:
	def __init__(self, line):
		cards = line.split(" ")
		self.mine = Hand(cards[:5])
		self.his = Hand(cards[5:])

	def winner(self):
		return self.mine > self.his

def read_rounds(file):
	open_file = open(file)
	lines = open_file.readlines()
	return [Round(line) for line in lines]

def main():
	rounds = read_rounds("data/poker.txt")
	count = sum(1 for round in rounds if round.winner())
	print(count)

main()