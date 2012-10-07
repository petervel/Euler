#!/usr/bin/python
__author__ = 'peter.vel'

def is_palindrome(string):
	if len(string) < 2:
		return True
	if string[0] != string[-1]:
		return False

	return is_palindrome(string[1:-1])

def is_double_palindrome(number):
	decimal = str(number)
	binary = bin(number)[2:]
	return is_palindrome(decimal) and is_palindrome(binary)

def main():
	sum = 0
	for i in range(1, 1000000):
		if is_double_palindrome(i):
			sum += i
	print(sum)

main()