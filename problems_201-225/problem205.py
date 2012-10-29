#!/usr/bin/python
__author__ = 'peter.vel'

from random import Random

rng = Random()

def play_game():
	peter = 0
	for i in range(9):
		peter += rng.randint(1, 4)

	colin = 0
	for i in range(6):
		colin += rng.randint(1, 6)

	return peter > colin

def main():
	peter = 0
	games = 0
	while True:
		if play_game():
			peter += 1
		games += 1

		print(float(peter)/games)

main()