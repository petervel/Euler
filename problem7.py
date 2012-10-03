#!/usr/bin/python
SIEVE_SIZE = 200000

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
	return list

def main():
	list = sieve()
	index = 0
	for i in list:
		if i >= 2:
			index += 1
		if index == 10001:
			print(i)
			return

main()