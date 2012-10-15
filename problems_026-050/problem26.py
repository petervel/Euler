#!/usr/bin/python
__author__ = 'peter.vel'

from decimal import *

def is_repeated(string, length):
	for i in range(1, int(len(string) / length)):
		if string[0 : length] != string[i * length : (i+1) * length]:
			return False
	return True

def cycle_length(number):
	string = str(number)[2:]

	half = int(len(string)/2)
	for j in range(1, half):
		for i in range(1, 20):
			if is_repeated(string[i:], j):
				return j

def main():
	setcontext(Context(prec=3000))

	record_holder = 0
	highest = 0
	for i in range(1, 1000):
		length = cycle_length(Decimal(1)/i)
		if length > highest:
			highest = length
			record_holder = i
	print(record_holder)

main()
