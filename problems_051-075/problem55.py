#!/usr/bin/python
__author__ = 'peter.vel'

def is_palindrome(string):
	if len(string) < 2:
		return True
	if string[0] != string[-1]:
		return False
	return is_palindrome(string[1:-1])

def reverse(number):
	string = str(number)
	return int(string[::-1])

def is_lychrel(number):
	for i in range(50):
		number += reverse(number)
		if is_palindrome(str(number)):
			return False
	return True

def main():
	count = 0
	is_lychrel(4994)
	for i in range(10000):
		if is_lychrel(i):
			print("found {0}".format(i))
			count += 1
	print(count)

main()
