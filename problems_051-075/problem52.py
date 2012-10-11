#!/usr/bin/python
__author__ = 'peter.vel'

def same_digits(number, other):
	if len(number) != len(other):
		return False

	return sorted(number) == sorted(other)

def is_special(number):
	string = str(number)
	if string[0] != '1':
		return False

	for i in range(2, 7):
		product = i * number
		if not same_digits(string, str(product)):
			return False
	return True

def main():
	for i in range(1, 1000000):
		if is_special(i):
			print(i)
			return

main()