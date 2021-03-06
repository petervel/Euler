#!/usr/bin/python
__author__ = 'peter.vel'

SIEVE_SIZE = 2000000

def create_list():
	return range(0, SIEVE_SIZE)

def remove_from_list(i, list):
	index = 2 * i
	while index < SIEVE_SIZE:
		list[index] = 0
		index += i

def sieve():
	list = create_list()
	for i in list:
		if i >= 2:
			remove_from_list(i, list)
		else:
			list[i] = 0
	return list

def main():
	list = sieve()
	sum = 0
	for i in list:
		sum += i
	print sum

main()