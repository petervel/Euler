#!/usr/bin/python
__author__ = 'peter.vel'

from datetime import datetime

def square_of_sums(rng):
	return sum(x for x in rng) ** 2

def sum_of_squares(rng):
	return sum(x ** 2 for x in rng)

def main():
	rng = range(1,101)
	print square_of_sums(rng) - sum_of_squares(rng)

main()