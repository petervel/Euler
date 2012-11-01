#!/usr/bin/python
__author__ = 'peter.vel'

#find the last 10 digits of 1^1 + 2^2 + 3^3 + .. 1000^1000

def main():
	numbers = [i**i for i in range(1, 1001)]
	total = sum(numbers)
	print(str(total)[-10:])

main()