#!/usr/bin/python
__author__ = 'peter.vel'

def list_contains(list, item):
	for i in list:
		if i == item:
			return True
	return False

def get_divisors(number):
	divisors = []
	half = int((number / 2) + 1)
	for i in range(1, half):
		if number % i == 0:
			divisors.append(i)
	return divisors

def is_abundant(number):
	divisors = get_divisors(number)
	sum = 0
	for i in divisors:
		sum += i
	return sum > number

def list_abundant_numbers(max):
	list = []
	for i in range(1, max):
		if is_abundant(i):
			list.append(i)
	return list

def is_sum_of_two_numbers(list, number):
	for i in list:
		if i >= number:
			return False

		other = number - i
		if list_contains(list, other):
			return True
	return False

def sum_numbers(list, numbers):
	sum = 0
	for i in numbers:
		if not is_sum_of_two_numbers(list, i):
			sum += i
	return sum

def main():
	list = list_abundant_numbers(28123)
	numbers = range(1, 28123)
	sum = sum_numbers(list, numbers)
	print(sum)

main()
