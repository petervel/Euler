#!/usr/bin/python
__author__ = 'peter.vel'

def digits(number):
	number = str(number)
	list = []
	for i in number:
		list.append(int(i))
	return list

def is_sum_of_fifths(number):
	sum = 0
	for i in digits(number):
		sum += pow(i, 5)
	return number == sum

def main():
	sum = 0
	for i in range(10, 1000000):
		if is_sum_of_fifths(i):
			print("* {0}".format(i))
			sum += i
	print(sum)

main()