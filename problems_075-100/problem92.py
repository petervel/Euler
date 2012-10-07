#!/usr/bin/python
__author__ = 'peter.vel'

def next_number(number):
	string = str(number)
	sum = 0
	for c in string:
		sum += pow(int(c), 2)
	return sum

def do_chain(number):
	if number == 1 or number == 89:
		return number
	next = next_number(number)
	return do_chain(next)

def main():
	count = 0
	for i in range(1, 10000000):
		if do_chain(i) == 89:
			count += 1
	print(count)

main()