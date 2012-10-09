#!/usr/bin/python
__author__ = 'peter.vel'

number_chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def is_prime(number):
	end = int(number ** 0.5) + 1
	for i in range(2, end):
		if number % i == 0:
			return False
	return True

def try_number(string, remaining_chars):
	if len(remaining_chars) == 0:
		if is_prime(int(string)):
			return string
		else:
			return None

	for i in remaining_chars:
		sub_list = list(remaining_chars)
		sub_list.remove(i)
		result = try_number(string + i, sub_list)
		if result != None:
			return result

def main():
	for i in range(9):
		chars = list(number_chars[:9-i])
		chars.reverse()
		result = try_number("", chars)
		if result is None:
			print("no results found with {0} digits".format(9-i))
		else:
			print(result)
			return


main()