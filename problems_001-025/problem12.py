#!/usr/bin/python
__author__ = 'peter.vel'

def count_divisors(number):
	count = 1
	for i in range(1,number/2):
		if number % i == 0:
			count += 1
	return count

def main():
	sum = 0
	highest = 0
	for i in range(1, 1000000):
		sum += i

		divisor_count = count_divisors(sum)

		if divisor_count > highest:
			highest = divisor_count
			print("{0}: {1}".format(sum, divisor_count))

		if divisor_count > 500:
			print sum
			return

main()

#TODO: this is ridiculously slow, rewrite this solution