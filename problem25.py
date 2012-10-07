#!/usr/bin/python
__author__ = 'peter.vel'

def digit_count(number):
	return len(str(number))

def first_fibonacci_with_digits(digits):
	i = 2
	prev = 1
	cur = 1
	while digit_count(cur) < 1000:
		next = prev + cur
		prev = cur
		cur = next
		i += 1
	return i

def main():
	print(first_fibonacci_with_digits(1000))

main()