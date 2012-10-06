#!/usr/bin/python
__author__ = 'peter.vel'

def sum_digits(number):
	number = str(number)
	sum = 0
	for i in number:
		sum += int(i)
	return sum

def fac(number):
	if number <= 1:
		return 1
	return number * fac(number - 1)

def main():
	print(sum_digits(fac(100)))

main()