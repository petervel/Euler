#!/usr/bin/python
__author__ = 'peter.vel'

def sum_divisors(number):
	sum = 1
	sqrt = number ** 0.5
	last = int(sqrt) + 1
	for i in range(2, last):
		if number % i == 0:
			sum += i
			sum += number / i

	if sqrt == int(sqrt):
		sum -= sqrt #added this one twice

	return sum

def main():
	sum = 0
	abundant_numbers = set()
	for i in range(1, 28123):
		if sum_divisors(i) > i:
			abundant_numbers.add(i)
		if not any( (i - a in abundant_numbers) for a in abundant_numbers):
			sum += i
	print(sum)

main()
