#!/usr/bin/python
__author__ = 'peter.vel'

number_chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def is_pandigital(string):
	if len(string) != 9:
		return False

	for i in number_chars:
		if not i in string:
			return False
	return True

def check_number(number):
	string = ""
	for i in range(1, 10):
		string += str(number * i)
		if len (string) > 9:
			return 0

		if len(string) < 9:
			continue

		if is_pandigital(string):
			return int(string)
		else:
			return 0
	return 0

def main():
	highest = 0
	record_holder = 0
	for i in range(1, 1000000):
		result = check_number(i)
		if result != 0 and result > highest:
			highest = result
			record_holder = i
	print("winner is {0} with {1}".format(record_holder, highest))

main()