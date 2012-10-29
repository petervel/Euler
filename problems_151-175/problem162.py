#!/usr/bin/python
__author__ = 'peter.vel'

def is_valid(str):
	return '0' in str and '1' in str and 'a' in str

def count_numbers():
	number = 1
	count = 0
	while True:
		hex_string = hex(number)

		if len(hex_string) > 16:
			break

		if is_valid(hex_string[2:]):
			print(hex_string)
			count += 1

		number += 1

	return count

def main():
	answer = count_numbers()
	print(hex(answer))

main()
