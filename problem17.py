#!/usr/bin/python
__author__ = 'peter.vel'

def digit_length(number):
	if number == 0:
		return 0
	elif number == 1 or number == 2 or number == 6:
		return 3
	elif number == 3 or number == 4 or number == 5 or number == 9:
		return 4
	elif number == 7 or number == 8:
		return 5
	else:
		return 0

def tens_length(number):
	if number == 2 or number == 3 or number == 9:
		return 6
	elif number == 4 or number == 5 or number == 6:
		return 5
	elif number == 7 or number == 8:
		return 7
	else:
		return 0

def text_length_hundreds(number):
	hundreds = int(number / 100)
	if hundreds == 0:
		return 0

	return digit_length(hundreds) + 7

def text_length_tens(number):
	number = number % 100 #strip hundreds
	number = int(number / 10) #strip ones, convert to single digit

	return tens_length(number)

def text_length_remainder(number):
	number = number % 100 #strip hundreds
	if number >= 20:
		number = number % 10

	if number < 10:
		return digit_length(number)
	if number == 10:
		return 3
	elif number == 11 or number == 12:
		return 6
	elif number == 13 or number == 14 or number == 19:
		return 8
	elif number == 15 or number == 16:
		return 7
	elif number == 17 or number == 18:
		return 9


def text_length(number):
	hundreds_length = text_length_hundreds(number)
	tens_length = text_length_tens(number)
	remainder_length = text_length_remainder(number)
	if hundreds_length != 0 and (tens_length != 0 or remainder_length != 0):
		hundreds_length += 3
	return hundreds_length + tens_length + remainder_length

def main():
	sum = 0
	for i in range(1, 1000):
		length = text_length(i)
		sum += length
		print("{0}: {1}".format(i, length))

	print("sum : {0}".format(sum))

main()
