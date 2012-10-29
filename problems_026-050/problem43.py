#!/usr/bin/python
__author__ = 'peter.vel'

digits = ['1','2','3','4','5','6','7','8','9','0']

def generate_pandigitals(remaining_digits):
	if len(remaining_digits) == 1:
		return remaining_digits[0]

	numbers = []
	for i in remaining_digits:
		sub_list = list(remaining_digits)
		sub_list.remove(i)
		for sub in generate_pandigitals(sub_list):
			numbers.append(i + sub)
	return numbers

def is_valid(number):
	if int(number[1:4]) % 2 != 0: return False
	if int(number[2:5]) % 3 != 0: return False
	if int(number[3:6]) % 5 != 0: return False
	if int(number[4:7]) % 7 != 0: return False
	if int(number[5:8]) % 11 != 0: return False
	if int(number[6:9]) % 13 != 0: return False
	if int(number[7:10]) % 17 != 0: return False
	return True

def filter(numbers):
	result = []
	for i in numbers:
		if is_valid(i):
			print(i)
			result.append(int(i))
	return result

def main():
	numbers = generate_pandigitals(digits)
	result = filter(numbers)
	print("---------- +")
	print(sum(result))

main()
