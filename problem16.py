#!/usr/bin/python
__author__ = 'peter.vel'

def sum_chars(number):
	number = str(number)
	sum = 0
	for i in range(0, len(number)):
		sum += int(number[i])

	return sum

def main():
	print pow(2,1000)
	print sum_chars(pow(2, 1000))

main()
